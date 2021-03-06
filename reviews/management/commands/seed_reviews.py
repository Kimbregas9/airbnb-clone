import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):

    help = "this command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="how many users do you want to create"
        )

    #overriding
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        user = user_models.User.objects.all()
        room = room_models.Room.objects.all()
    
        seeder.add_entity(review_models.Review, number, 
            {
                "accurancy" : lambda x : random.randint(0,6),
                "communication" : lambda x : random.randint(0,6),
                "cleaniness" : lambda x : random.randint(0,6),
                "location" : lambda x : random.randint(0,6),
                "check_in" : lambda x : random.randint(0,6),
                "value" : lambda x : random.randint(0,6),
                "room" : lambda x : random.choice(room),
                "user" : lambda x : random.choice(user),
            }
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))