from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# Import gallery_view explicitly
from .views import gallery_view

urlpatterns = [
    path('api/register/player/', views.RegisterPlayerView.as_view(), name='register-player'),
    path('api/register/manager/', views.RegisterManagerView.as_view(), name='register-manager'),
    path('', views.home_view, name='home'),
    path('fixtures/', views.fixture_view, name='fixtures'),
    path('register/', views.registration_view, name='register'),
    path('ranking/', views.ranking_view, name='ranking'),
    path('gallery/', gallery_view, name='gallery'),  # now gallery_view is defined here
]
