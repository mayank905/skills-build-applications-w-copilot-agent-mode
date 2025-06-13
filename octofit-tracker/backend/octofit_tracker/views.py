# Views for OctoFit Tracker
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    # Return full URLs for codespace and localhost
    base_urls = [
        'https://probable-disco-p7jqx56prrw2rxj4-8000.app.github.dev/api/',
        'http://localhost:8000/api/'
    ]
    return Response({
        'users': [url + 'users/' for url in base_urls],
        'teams': [url + 'teams/' for url in base_urls],
        'activity': [url + 'activity/' for url in base_urls],
        'leaderboard': [url + 'leaderboard/' for url in base_urls],
        'workouts': [url + 'workouts/' for url in base_urls],
    })
