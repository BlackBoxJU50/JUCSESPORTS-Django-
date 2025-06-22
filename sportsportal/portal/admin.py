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
    InventoryItem,
    Donation,
)

# --- Players ---
@admin.register(BadmintonPlayer)
class BadmintonPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')
    search_fields = ('user__username', 'team_name', 'email')


@admin.register(CricketPlayer)
class CricketPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')
    search_fields = ('user__username', 'team_name', 'email')


@admin.register(FootballPlayer)
class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name', 'email')
    search_fields = ('user__username', 'team_name', 'email')


# --- Managers ---
@admin.register(BadmintonManager)
class BadmintonManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')
    search_fields = ('user__username', 'team_name')


@admin.register(CricketManager)
class CricketManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')
    search_fields = ('user__username', 'team_name')


@admin.register(FootballManager)
class FootballManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team_name')
    search_fields = ('user__username', 'team_name')


# --- Fixtures ---
@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('date', 'teams', 'result', 'game')
    list_filter = ('game',)
    search_fields = ('teams',)
    ordering = ('-date',)


# --- Rankings ---
@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'sport', 'is_previous')
    list_filter = ('sport', 'is_previous')
    search_fields = ('name',)
    ordering = ('-points',)


# --- Gallery ---
@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


# --- Inventory ---
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'status', 'sport', 'added_on')
    list_filter = ('status', 'sport')
    search_fields = ('name',)
    ordering = ('-added_on',)


# --- Donations ---
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch', 'amount', 'method', 'created_at')
    list_filter = ('method', 'batch')
    search_fields = ('name', 'batch')
    ordering = ('-created_at',)
