from django.urls import path
from . import views



urlpatterns = [
    path('', views.diary_entries, name='diary_entries'),
    path('create/', views.create_diary_entry, name='create_diary_entry'),
]