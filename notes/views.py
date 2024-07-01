from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from .forms import CreateNoteForm
from .models import Note


class UserNotesView(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts:login'
    template_name = "notes/user_notes.html"
    context_object_name = "user_notes"

    def get_queryset(self):
        return Note.objects.filter(user__username=self.request.user)


class CreateNoteView(LoginRequiredMixin, generic.CreateView):
    login_url = 'accounts:login'
    model = Note
    template_name = "notes/create_note.html"
    form_class = CreateNoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note_edit.html'
    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = self.object  # Додати об'єкт нотатки до контексту
        return context


class NoteDeleteView(DeleteView):
    model = Note

    success_url = reverse_lazy('notes:user_notes')


