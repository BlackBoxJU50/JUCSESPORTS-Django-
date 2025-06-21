from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import InventoryForm
from django.db import IntegrityError
from .models import (
    BadmintonPlayer,
    CricketPlayer,
    FootballPlayer,
    BadmintonManager,
    CricketManager,
    FootballManager,
    Fixture,
    Game,
    Ranking,
    GalleryItem,
    InventoryItem,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


class RegisterPlayerView(APIView):
    def post(self, request):
        game = request.data.get('game_name')
        username = request.data.get('user')
        team_name = request.data.get('team_name')
        email = request.data.get('email')
        image = request.FILES.get('image')

        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password("defaultpassword")
            user.save()

        try:
            if game == "Badminton":
                BadmintonPlayer.objects.update_or_create(
                    user=user,
                    defaults={'team_name': team_name, 'email': email, 'image': image}
                )
            elif game == "Cricket":
                CricketPlayer.objects.update_or_create(
                    user=user,
                    defaults={'team_name': team_name, 'email': email, 'image': image}
                )
            elif game == "Football":
                FootballPlayer.objects.update_or_create(
                    user=user,
                    defaults={'team_name': team_name, 'email': email, 'image': image}
                )
            else:
                return Response({'error': 'Invalid game name.'}, status=HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'error': f"Player for user '{username}' already exists."}, status=HTTP_400_BAD_REQUEST)

        return Response({'message': f"Player registered successfully for {game}."}, status=HTTP_201_CREATED)


class RegisterManagerView(APIView):
    def post(self, request):
        game_name = request.data.get('game_name')
        username = request.data.get('user')
        team_name = request.data.get('team_name')
        image = request.FILES.get('image')

        game, _ = Game.objects.get_or_create(name=game_name)

        user, _ = User.objects.get_or_create(username=username)
        user.set_password("defaultpassword")
        user.save()

        if BadmintonManager.objects.filter(team_name=team_name).exists() or \
           CricketManager.objects.filter(team_name=team_name).exists() or \
           FootballManager.objects.filter(team_name=team_name).exists():
            return Response({'error': f"A manager for '{team_name}' already exists."}, status=HTTP_400_BAD_REQUEST)

        if game_name == "Badminton":
            BadmintonManager.objects.create(user=user, team_name=team_name, game=game, image=image)
        elif game_name == "Cricket":
            CricketManager.objects.create(user=user, team_name=team_name, game=game, image=image)
        elif game_name == "Football":
            FootballManager.objects.create(user=user, team_name=team_name, game=game, image=image)
        else:
            return Response({'error': 'Invalid game name.'}, status=HTTP_400_BAD_REQUEST)

        game.team_count += 1
        game.save()

        return Response({'message': f"Manager registered successfully for {game_name}. Total teams: {game.team_count}."}, status=HTTP_201_CREATED)


def fixture_view(request):
    selected_game = request.GET.get('game', 'Badminton')

    if selected_game == "Badminton":
        players = BadmintonPlayer.objects.all()
        managers = BadmintonManager.objects.all()
    elif selected_game == "Cricket":
        players = CricketPlayer.objects.all()
        managers = CricketManager.objects.all()
    elif selected_game == "Football":
        players = FootballPlayer.objects.all()
        managers = FootballManager.objects.all()
    else:
        players = []
        managers = []

    fixtures = Fixture.objects.filter(game=selected_game)

    return render(request, 'fixtures.html', {
        'game': selected_game,
        'fixtures': fixtures,
        'players': players,
        'managers': managers,
    })


def registration_view(request):
    return render(request, 'registration.html')


def ranking_view(request):
    rankings = Ranking.objects.all().order_by('-points')  # highest points first
    sports = ['Badminton', 'Cricket', 'Football']
    return render(request, 'ranking.html', {'rankings': rankings, 'sports': sports})



def home_view(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})


def gallery_view(request):
    current_items = GalleryItem.objects.filter(category='current')
    previous_items = GalleryItem.objects.filter(category='previous')
    return render(request, 'gallery.html', {
        'current_items': current_items,
        'previous_items': previous_items
    })


def inventory_view(request):
    selected_sport = request.GET.get('sport', 'All')

    if selected_sport == 'All':
        items = InventoryItem.objects.all().order_by('-added_on')
    else:
        items = InventoryItem.objects.filter(sport=selected_sport).order_by('-added_on')

    form = InventoryForm(request.POST or None) if request.user.is_staff else None

    if request.method == 'POST' and form and form.is_valid():
        form.save()
        return redirect('inventory')

    context = {
        'form': form,
        'items': items,
        'selected_sport': selected_sport,
        'sports': ['All', 'Badminton', 'Cricket', 'Football'],
    }
    return render(request, 'inventory.html', context)


@user_passes_test(lambda u: u.is_staff)
def delete_inventory_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    item.delete()
    return redirect('inventory')
