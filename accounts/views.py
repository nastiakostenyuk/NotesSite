from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView


from .forms import CreateUserForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse('notes:user_notes')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class UserSignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse("accounts:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log in the newly created user
        messages.success(self.request, f'User {user.username} was created successfully')
        return super().form_valid(form)
