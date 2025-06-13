from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Populating the octofit_db database with test data for users, teams, activities, leaderboards, and workouts.
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams (store user emails in members JSONField)
        team1 = Team.objects.create(name='Team Alpha', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Beta', members=[user3.email])

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='cycle', duration=60, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        # Workouts
        Workout.objects.create(user=user1, workout_type='cardio', details='5km run', date=timezone.now())
        Workout.objects.create(user=user2, workout_type='strength', details='Upper body', date=timezone.now())
        Workout.objects.create(user=user3, workout_type='yoga', details='Morning session', date=timezone.now())
        
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
