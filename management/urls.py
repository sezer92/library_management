from django.urls import path, include
from rest_framework import routers
from management import views


# Router for REST API
router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'cds', views.CdViewSet)
router.register(r'dvds', views.DvdViewSet)

# URL patterns for librarian and member application
urlpatterns = [
    path('', views.list_members, name='list_members'),
    path('create_member/', views.create_member, name='create_member'),
    path('update_member/<int:member_id>/', views.update_member, name='update_member'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    path('add_media/', views.add_media, name='add_media'),
    path('list_media/', views.list_media, name='list_media'),
    path('list_available_media/', views.list_available_media, name='list_available_media'),
    path('create_borrow/<int:media_id>/', views.create_borrow, name='create_borrow'),
    path('return_borrow/<int:media_id>/', views.return_borrow, name='return_borrow'),
    path('api/', include(router.urls)),
]