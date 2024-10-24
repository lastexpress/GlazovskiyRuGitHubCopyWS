from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from account import views
from .views import LoginView, RegistrationView, AccountView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('my/', views.AccountView, name='account'),
    path('edit/', views.edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)