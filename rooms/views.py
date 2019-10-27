from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all() #lazy just making queryset, not db hit
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.get_page(page)

    return render(request, "rooms/home.html", context={
        "page":rooms
    })
