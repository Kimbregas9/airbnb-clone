from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accurancy = models.ImageField()
    communication = models.ImageField()
    cleaniness = models.ImageField()
    location = models.ImageField()
    check_in = models.ImageField()
    value = models.ImageField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
