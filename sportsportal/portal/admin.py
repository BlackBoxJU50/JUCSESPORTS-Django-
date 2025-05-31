from django.contrib import admin
from .models import (
    BadmintonPlayer,
    CricketPlayer,
    FootballPlayer,
    BadmintonManager,
    CricketManager,
    FootballManager,
<<<<<<< HEAD
    Fixture,
    Ranking,
=======
    Fixture
>>>>>>> 38df760278b7659d258db4ec363ed2a96c91c2e5
)

# Register each model individually
@admin.register(BadmintonPlayer)
class BadmintonPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')

@admin.register(CricketPlayer)
class CricketPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')

@admin.register(FootballPlayer)
class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')

@admin.register(BadmintonManager)
class BadmintonManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')

@admin.register(CricketManager)
class CricketManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')

@admin.register(FootballManager)
class FootballManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')

@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('date', 'teams', 'result', 'game')
<<<<<<< HEAD

# ✅ Updated RankingAdmin to include 'is_previous'
@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'sport', 'is_previous')  # Added is_previous
    list_filter = ('sport', 'is_previous')  # Optional: filter by sport and type
    search_fields = ('name',)  # Optional: search by player name
=======
>>>>>>> 38df760278b7659d258db4ec363ed2a96c91c2e5
