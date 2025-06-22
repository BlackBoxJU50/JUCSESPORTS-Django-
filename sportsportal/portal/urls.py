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
    path('gallery/', views.gallery_view, name='gallery'),
    path('inventory/', views.inventory_view, name='inventory'),  
    path('inventory/delete/<int:item_id>/', views.delete_inventory_item, name='delete_inventory'),
     path('donation/', views.donation_page, name='donation'),  
]
