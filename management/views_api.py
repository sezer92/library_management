from rest_framework import viewsets
from .models import Member, Book, Cd, Dvd
from .serializers import MemberSerializer, BookSerializer, CdSerializer, DvdSerializer

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
