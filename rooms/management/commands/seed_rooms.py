import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):

    help = "this command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="how many users do you want to create"
        )

    #overriding
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        
        all_users = user_models.User.objects.all() #foreign key .... also it is not good method to get all users
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(room_models.Room, number, {
            "name": lambda x:seeder.faker.address(),
            "host": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "guests": lambda x: random.randint(1, 20),
            "price": lambda x: random.randint(1, 300),
            "beds": lambda x: random.randint(1, 5),
            "bedrooms": lambda x: random.randint(1, 5),
            "baths": lambda x: random.randint(1, 5)
        })

        created_photos = seeder.execute()

        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amentity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk) #pk = primary key
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption = seeder.faker.sentence(),
                    room = room,
                    file = f"room_photos/{random.randint(1,31)}.webp"
                )

            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a) # many to many relationship

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f) # many to many relationship

            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r) # many to many relationship

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))