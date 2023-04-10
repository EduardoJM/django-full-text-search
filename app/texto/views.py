from django.shortcuts import render
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
    SearchHeadline,
)
from .models import Music, Singer

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


def search_music(request):
    term = request.GET.get('q')
    musics = None
    if term:
        vector = SearchVector("title", "singer__name", "content", config="portuguese")
        query = SearchQuery(term, config="portuguese")
        musics = Music.objects.annotate(
            search=vector,
            rank=SearchRank(
                vector,
                query,
            ),
            headline=SearchHeadline(
                "content",
                query,
                start_sel='<span>',
                stop_sel="</span>",
            ),
            similarity=TrigramSimilarity("content", term),
        ).filter(
            Q(search=term) | Q(similarity__gt=0)
        ).order_by("-rank", "-similarity").all()
    else:
        musics = Music.objects.order_by("-id").all()

    context = {
        'musics': musics,
        'term': term,
    }
    return render(request, "musicas.html", context)
