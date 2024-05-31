from django.urls import path
from django.views.generic import ListView, DetailView

from . import views
from . import models

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('world-time/', views.world_time_view, name='world-time'),
    path('calendar/<int:month>/', views.calendar_view, name='calendar'),
    path('notes/', views.notes_view, name='notes'),
    path('note/<int:pk>/', views.note_detail_view, name='note'),
    path('categories/', ListView.as_view(model=models.CategoryNote), name='categories'),
    path('category/<int:pk>/', DetailView.as_view(model=models.CategoryNote), name='category'),
    path('add-note/', views.NoteCreateView.as_view(), name='add-note'),
    path('add-category/', views.CategoryCreateView.as_view(), name='add-category'),
    path('update-note/<int:pk>/', views.NoteUpdateView.as_view(), name='update-note'),
    path('update-category/<int:pk>/', views.CategoryUpdateView.as_view(), name='update-category'),
    path('delete-note/<int:pk>/', views.NoteDeleteView.as_view(), name='delete-note'),
    path('delete-category/<int:pk>/', views.CategoryNoteDeleteView.as_view(), name='delete-category'),
]
