from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):

    #overriding
    def handle(self, *args, **options):

        help = "This command creates facilities"

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for item in facilities:
            Facility.objects.create(name=item)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created'))