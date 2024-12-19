from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MemberViewSet, BookViewSet, CdViewSet, DvdViewSet
from . import views


router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'books', BookViewSet)
router.register(r'cds', CdViewSet)
router.register(r'dvds', DvdViewSet)

app_name = 'bibliothecaire'

urlpatterns = [

    path('', views.home, name='home'),

    # Gestion des membres
    path('members/', views.list_members, name='list_members'),
    path('members/add/', views.create_member, name='create_member'),
    path('members/update/<int:member_id>/', views.update_member, name='update_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('', views.list_members, name='home'),


    # Gestion des médias
    path('media/', views.list_media, name='list_media'),
    path('media/add/', views.add_media, name='add_media'),

    # Gestion des emprunts et des retours
    path('borrow/<int:media_id>/', views.create_borrow, name='create_borrow'),
    path('return/<int:media_id>/', views.return_borrow, name='return_borrow'),
]
