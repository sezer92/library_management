from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Member, Book, Cd, Dvd, BoardGame

def home(request):
    return render(request, 'bibliothecaire/home.html')

# Gestion des membres
def list_members(request):
    members = Member.objects.all()
    return render(request, 'bibliothecaire/list_members.html', {'members': members})

def create_member(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Member.objects.create(name=name)
        messages.success(request, f"Member '{name}' has been created.")
        return redirect('bibliothecaire:list_members')
    return render(request, 'bibliothecaire/create_member.html')

def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.name = request.POST.get("name")
        member.save()
        messages.success(request, f"Member '{member.name}' has been updated.")
        return redirect('bibliothecaire:list_members')
    return render(request, 'bibliothecaire/update_member.html', {'member': member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    messages.success(request, f"Member '{member.name}' has been deleted.")
    return redirect('bibliothecaire:list_members')

# Gestion des médias
def list_media(request):
    books = Book.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request, 'bibliothecaire/list_media.html', {
        'books': books, 'cds': cds, 'dvds': dvds, 'boardgames': boardgames
    })

def add_media(request):
    if request.method == "POST":
        media_type = request.POST.get("media_type")
        name = request.POST.get("name")
        creator_or_author = request.POST.get("creator_or_author")
        if media_type == "book":
            Book.objects.create(name=name, author=creator_or_author)
        elif media_type == "cd":
            Cd.objects.create(name=name, artist=creator_or_author)
        elif media_type == "dvd":
            Dvd.objects.create(name=name, director=creator_or_author)
        elif media_type == "boardgame":
            BoardGame.objects.create(name=name, creator=creator_or_author)
        messages.success(request, f"Media '{name}' has been added.")
        return redirect('bibliothecaire:list_media')
    return render(request, 'bibliothecaire/add_media.html')

# Gestion des emprunts
def create_borrow(request, media_id):
    media_type = request.POST.get("media_type")  # Identifier le type de média
    if media_type == "book":
        media = get_object_or_404(Book, id=media_id)
    elif media_type == "cd":
        media = get_object_or_404(Cd, id=media_id)
    elif media_type == "dvd":
        media = get_object_or_404(Dvd, id=media_id)
    elif media_type == "boardgame":
        media = get_object_or_404(BoardGame, id=media_id)
    else:
        messages.error(request, "Type de média invalide.")
        return redirect('bibliothecaire:list_media')

    member = get_object_or_404(Member, id=request.POST.get("member_id"))

    if member.can_borrow() and media.available:
        # Marquer le média comme emprunté
        media.available = False
        media.save()

        # Augmenter le nombre d'emprunts du membre
        member.borrow_count += 1
        member.save()
        messages.success(request, f"Le média '{media.title}' a été emprunté par {member.name}.")
    else:
        messages.error(request, "Impossible d'emprunter ce média.")
    return redirect('bibliothecaire:list_media')



def return_borrow(request, media_id):
    media_type = request.POST.get("media_type")  # Identifier le type de média
    if media_type == "book":
        media = get_object_or_404(Book, id=media_id)
    elif media_type == "cd":
        media = get_object_or_404(Cd, id=media_id)
    elif media_type == "dvd":
        media = get_object_or_404(Dvd, id=media_id)
    elif media_type == "boardgame":
        media = get_object_or_404(BoardGame, id=media_id)
    else:
        messages.error(request, "Type de média invalide.")
        return redirect('bibliothecaire:list_media')

    # Marquer le média comme disponible
    media.available = True
    media.save()

    # Réduire le nombre d'emprunts du membre
    member = get_object_or_404(Member, id=request.POST.get("member_id"))
    member.borrow_count -= 1
    member.save()
    messages.success(request, f"Le média '{media.title}' a été rendu par {member.name}.")
    return redirect('bibliothecaire:list_media')


