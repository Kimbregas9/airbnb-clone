import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):

    help = "this command creates many reservations"

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
    
        seeder.add_entity(reservation_models.Reservation, number, 
            {
                "status" : lambda x : random.choice(["pending",
                                                     "confirmed",
                                                    "canceled"]),
                "room" : lambda x : random.choice(room),
                "guest" : lambda x : random.choice(user),
                "check_in" : lambda x : datetime.now(),
                "check_out" : lambda x : datetime.now() + 
                                        timedelta(days=random.randint(3,25)),
            }
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))