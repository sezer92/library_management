from rest_framework import serializers
from .models import Member, Book, Cd, Dvd, BoardGame

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cd
        fields = '__all__'

class DvdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dvd
        fields = '__all__'

# Ajouter le serializer pour BoardGame
class BoardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardGame
        fields = '__all__'

