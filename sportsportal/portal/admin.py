from django.contrib import admin
from .models import (
    BadmintonPlayer,
    CricketPlayer,
    FootballPlayer,
    BadmintonManager,
    CricketManager,
    FootballManager,
    Fixture,
    Ranking,
    GalleryItem,  
)

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

@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'sport', 'is_previous')
    list_filter = ('sport', 'is_previous')
    search_fields = ('name',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
