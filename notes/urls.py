from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('', views.UserNotesView.as_view(), name='user_notes'),
    path('create/', views.CreateNoteView.as_view(), name='create_note'),
    path('<int:pk>/', views.NoteUpdateView.as_view(), name='detail_note'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note')

]
