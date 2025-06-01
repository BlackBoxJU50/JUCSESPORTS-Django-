from django.db import models
from django.contrib.auth.models import User

# Abstract BasePlayer class for Players
class BasePlayer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(default="default@example.com")
    team_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)  # ✅ Added image field

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
<<<<<<< HEAD

class Ranking(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    sport = models.CharField(max_length=50)
    is_previous = models.BooleanField(default=False)  # ← Add this line if it's missing

    def __str__(self):
        return f"{self.name} - {self.sport} ({'Previous' if self.is_previous else 'Recent'})"
=======
>>>>>>> 38df760278b7659d258db4ec363ed2a96c91c2e5
