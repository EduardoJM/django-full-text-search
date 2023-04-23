from django.shortcuts import render
from .models import Singer

def search_singer(request):
    term = request.GET.get('q', None)
    singers = Singer.objects.search(term)

    context = {
        'singers': singers,
        'term': term,
    }
    return render(request, "cantor.html", context)
