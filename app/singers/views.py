from django.shortcuts import render
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from .models import Singer

def search_singer(request):
    term = request.GET.get('q')
    if term:
        vector = SearchVector("name", config="portuguese")
        query = SearchQuery(term, config="portuguese")
        singers = Singer.objects.annotate(
            search=vector,
            rank=SearchRank(vector, query),
            similarity=TrigramSimilarity("name", term),
        ).filter(
            Q(search=query) | Q(similarity__gt=0)
        ).order_by("-rank", "-similarity").all()
    else:
        singers = Singer.objects.order_by("-id").all()

    context = {
        'singers': singers,
        'term': term,
    }
    return render(request, "cantor.html", context)
