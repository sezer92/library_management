from django.contrib import admin
from .models import Member, Book, Cd, Dvd, BoardGame, Borrow

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'blocked', 'borrow_count', 'unblock_date')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('member', 'media', 'borrow_date', 'return_date', 'is_returned')
