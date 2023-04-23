from django.utils.translation import gettext_lazy as _
from django.template import loader
from django.utils.encoding import force_str
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from rest_framework.filters import BaseFilterBackend
from rest_framework.settings import api_settings
from rest_framework.compat import coreapi, coreschema

class FullTextSearchFilter(BaseFilterBackend):
    search_param = api_settings.SEARCH_PARAM
    template = 'rest_framework/filters/search.html'
    search_title = _('Search')
    search_description = _('A search term.')

    def get_config(self, view, request):
        return getattr(view, "search_config", None)

    def get_search_fields(self, view, request):
        return getattr(view, "search_fields", None)

    def get_similarity_threshold(self, view, request):
        return getattr(view, "similarity_threshold", 0)

    def get_search_term(self, request):
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        return params

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_term = self.get_search_term(request)
        config = self.get_config(view, request)
        threshold = self.get_similarity_threshold(view, request)

        if not search_term or not search_fields:
            return queryset

        search_vector = SearchVector(*search_fields, config=config)
        search_query = SearchQuery(search_term, config=config)

        queryset = queryset.annotate(
            search=search_vector,
            rank=SearchRank(
                search_vector,
                search_query,
            ),
            similarity=TrigramSimilarity(*search_fields, search_term),
        ).filter(
            Q(search=search_query) | Q(similarity__gt=threshold)
        ).order_by("-rank", "-similarity")

        return queryset

    def to_html(self, request, queryset, view):
        if not getattr(view, 'search_fields', None):
            return ''

        term = self.get_search_term(request)
        context = {
            'param': self.search_param,
            'term': term
        }
        template = loader.get_template(self.template)
        return template.render(context)

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.search_param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title=force_str(self.search_title),
                    description=force_str(self.search_description)
                )
            )
        ]

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': self.search_param,
                'required': False,
                'in': 'query',
                'description': force_str(self.search_description),
                'schema': {
                    'type': 'string',
                },
            },
        ]
