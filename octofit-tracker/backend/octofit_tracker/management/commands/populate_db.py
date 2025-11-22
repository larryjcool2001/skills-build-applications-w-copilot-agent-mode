
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')

        # Create teams and add members
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        marvel.members.add(ironman)
        dc.members.add(batman)

        # Create activities
        Activity.objects.create(user=ironman, activity_type='run', duration=30, distance=5.0)
        Activity.objects.create(user=batman, activity_type='cycle', duration=45, distance=20.0)

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, total_distance=5.0)
        Leaderboard.objects.create(user=batman, total_distance=20.0)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
