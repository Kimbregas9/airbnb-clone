from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amentity)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields" : ("name", "description", "country", "address", "price")}
        ),
        (
            "Times",
            {"fields" : ("check_in", "check_out", "instant_book")}
        ),
        (
            "More About the Spaces",
            {
                "classes" : ("collapse",),
                "fields" : ("amenities","facilities","house_rules")
            }
        ),
        (
            "Spaces",
            {"fields" : ("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "Last Detatils",
            {"fields" : ("host",)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    ordering = ('name', 'price', 'bedrooms')

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules", 
        "city", 
        "country"
    )

    search_fields = ("=city","^host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj): #self <- admin class obj <-now row
        print(obj.amenities.all())
        return "Potato"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition """

    pass