from django.contrib import admin
from .models import (
    BadmintonPlayer,
    CricketPlayer,
    FootballPlayer,
    BadmintonManager,
    CricketManager,
    FootballManager,
    Fixture
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
