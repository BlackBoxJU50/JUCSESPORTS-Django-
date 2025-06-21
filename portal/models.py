from django.db import models
from django.contrib.auth.models import User

# Abstract BasePlayer class for Players
class BasePlayer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(default="default@example.com")
    team_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)  

    class Meta:
        abstract = True  # This serves as the base for individual game player tables

    def __str__(self):
        return f"{self.user.username} - {self.team_name}"
    
class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team_count = models.IntegerField(default=0)  # Tracks registered teams

    def __str__(self):
        return f"{self.name} ({self.team_count} teams)"

# Abstract BaseManager class for Managers
class BaseManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    team_name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='manager_images/', null=True, blank=True)  # ✅ Added image field

    class Meta:
        abstract = True  # This serves as the base for individual game manager tables

    def __str__(self):
        return f"{self.user.username} - {self.team_name} ({self.game.name})"

# Badminton Player and Manager Models
class BadmintonPlayer(BasePlayer):
    pass

class BadmintonManager(BaseManager):
    pass

# Cricket Player and Manager Models
class CricketPlayer(BasePlayer):
    pass

class CricketManager(BaseManager):
    pass

# Football Player and Manager Models
class FootballPlayer(BasePlayer):
    pass

class FootballManager(BaseManager):
    pass

# Guest Model
class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="default@example.com")

    def __str__(self):
        return self.name

# Fixture Model
class Fixture(models.Model):
    date = models.DateField()
    teams = models.CharField(max_length=255)
    result = models.CharField(max_length=255, blank=True, null=True)
    game = models.CharField(max_length=50, choices=[
        ('Badminton', 'Badminton'),
        ('Cricket', 'Cricket'),
        ('Football', 'Football')
    ])

    def __str__(self):
        return f"{self.teams} ({self.game}) - {self.date}"

class Ranking(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    sport = models.CharField(max_length=50)
    is_previous = models.BooleanField(default=False)  # ← Add this line if it's missing

    def __str__(self):
        return f"{self.name} - {self.sport} ({'Previous' if self.is_previous else 'Recent'})"

class InventoryItem(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Damaged', 'Damaged'),
    ]

    SPORT_CHOICES = [
        ('Badminton', 'Badminton'),
        ('Cricket', 'Cricket'),
        ('Football', 'Football'),
    ]

    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='Badminton')  # Added sport field
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('current', 'Current Year'),
        ('previous', 'Previous Year'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)  # For YouTube or hosted videos
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
