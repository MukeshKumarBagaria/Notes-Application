from django.urls import path
from notes.views import get_routes, get_notes, get_note,createNote,updateNote,deleteNote

urlpatterns = [
    path('', get_routes, name='routes'),
    path('notes/', get_notes, name='notes'),
    path('notes/<int:pk>', get_note, name='notes'),
    path('notes/create/', createNote, name='create'),
    path('notes/<int:pk>/update/', updateNote, name='update'),
    path('notes/<int:pk>/delete/', deleteNote, name='delete'),

    
]
