from django.urls import path
from . import views

app_name = 'membre'

urlpatterns = [
    # Consultation des médias disponibles
    path('media/', views.list_available_media, name='list_available_media'),
    path('', views.list_available_media, name='home'),


]
