from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('signup/', views.UserSignUpView.as_view(), name='signup')
]
