from django.shortcuts import render
from membre.models import Book, Cd, Dvd, BoardGame

def list_available_media(request):
    books = Book.objects.filter(available=True)
    cds = Cd.objects.filter(available=True)
    dvds = Dvd.objects.filter(available=True)
    boardgames = BoardGame.objects.filter(available=True)
    return render(request, 'membre/list_available_media.html', {
        'books': books,
        'cds': cds,
        'dvds': dvds,
        'boardgames': boardgames,
    })

