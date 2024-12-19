from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Member, Book, Cd, Dvd, BoardGame
from django.contrib import messages
import logging
from rest_framework import viewsets
from bibliothecaire.serializers import MemberSerializer, BookSerializer, CdSerializer, DvdSerializer
from celery import shared_task

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Views for librarian application

def create_member(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Member.objects.create(name=name)
        logger.info(f"Created member: {name}")
        messages.success(request, f"Member '{name}' has been successfully created.")
        return redirect('list_members')
    return render(request, 'management/create_member.html')

def list_members(request):
    members = Member.objects.all()
    return render(request, 'management/list_members.html', {'members': members})

def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.name = request.POST.get("name")
        member.save()
        logger.info(f"Updated member: {member.name}")
        messages.success(request, f"Member '{member.name}' has been successfully updated.")
        return redirect('list_members')
    return render(request, 'management/update_member.html', {'member': member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    logger.info(f"Deleted member: {member.name}")
    member.delete()
    messages.success(request, f"Member '{member.name}' has been successfully deleted.")
    return redirect('list_members')

def create_borrow(request, media_id):
    member = get_object_or_404(Member, id=request.POST.get("member_id"))
    media = get_object_or_404(Book, id=media_id)  # Replace 'Book' with the correct model type (Book, Cd, Dvd)

    if member.can_borrow() and media.available:
        media.borrow_date = timezone.now().date()
        media.available = False
        media.save()

        member.borrow_count += 1
        member.save()

        logger.info(f"Borrow created for {member.name} - Media: {media.name}")
        messages.success(request, f"Media '{media.name}' has been successfully borrowed by {member.name}.")
        return redirect('list_members')
    messages.error(request, "The member cannot borrow more media or the media is not available.")
    return redirect('list_members')

def return_borrow(request, media_id):
    media = get_object_or_404(Book, id=media_id)  # Replace 'Book' with the correct model type (Book, Cd, Dvd)
    member = get_object_or_404(Member, id=request.POST.get("member_id"))

    if not media.available:
        media.available = True
        media.save()

        member.borrow_count -= 1
        member.save()

        logger.info(f"Borrow returned for {member.name} - Media: {media.name}")
        messages.success(request, f"Media '{media.name}' has been successfully returned by {member.name}.")
        return redirect('list_members')
    messages.error(request, "This media was not borrowed.")
    return redirect('list_members')

# View to add new media
def add_media(request):
    if request.method == "POST":
        media_type = request.POST.get("media_type")
        name = request.POST.get("name")
        creator_or_author = request.POST.get("creator_or_author")
        if media_type == "book":
            Book.objects.create(name=name, author=creator_or_author)
            messages.success(request, f"Book '{name}' by {creator_or_author} has been successfully added.")
        elif media_type == "cd":
            Cd.objects.create(name=name, artist=creator_or_author)
            messages.success(request, f"CD '{name}' by {creator_or_author} has been successfully added.")
        elif media_type == "dvd":
            Dvd.objects.create(name=name, director=creator_or_author)
            messages.success(request, f"DVD '{name}' by {creator_or_author} has been successfully added.")
        elif media_type == "boardgame":
            BoardGame.objects.create(name=name, creator=creator_or_author)
            messages.success(request, f"Board Game '{name}' by {creator_or_author} has been successfully added.")
        else:
            messages.error(request, "Invalid media type.")
        return redirect('list_media')
    return render(request, 'management/add_media.html')

# View to list all media
def list_media(request):
    books = Book.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request, 'management/list_media.html', {'books': books, 'cds': cds, 'dvds': dvds, 'boardgames': boardgames})

def list_available_media(request):
    # Filtrer les médias disponibles (livres, CDs, DVDs, jeux de plateau)
    available_books = Book.objects.filter(available=True)
    available_cds = Cd.objects.filter(available=True)
    available_dvds = Dvd.objects.filter(available=True)
    available_board_games = BoardGame.objects.filter(available=True)

    context = {
        'available_books': available_books,
        'available_cds': available_cds,
        'available_dvds': available_dvds,
        'available_board_games': available_board_games,
    }
    return render(request, 'management/list_available_media.html', context)



# REST API ViewSets using Django Rest Framework

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CdViewSet(viewsets.ModelViewSet):
    queryset = Cd.objects.all()
    serializer_class = CdSerializer

class DvdViewSet(viewsets.ModelViewSet):
    queryset = Dvd.objects.all()
    serializer_class = DvdSerializer

# Asynchronous Task to Check for Overdue Members

@shared_task
def check_overdue_members():
    for member in Member.objects.all():
        if member.borrow_count > 0 and member.unblock_date and member.unblock_date < timezone.now().date():
            member.blocked = True
            member.save()
            logger.info(f"Member {member.name} has been blocked due to overdue borrows.")
