from django.shortcuts import render
from .models import Genre, movies

def list_movies(request):
    context = {}
    context["movies"] = movies.objects.all()
    context["genres"] = Genre.objects.all()

    if request.method == 'POST':
        filtered_genre = request.POST.get('genres')
        filtered_language = request.POST.get('language')
        context["movies"] = movies.objects.filter(
            genre=filtered_genre,
            language=filtered_language
        )
    return render(request, "movies.html", context)

