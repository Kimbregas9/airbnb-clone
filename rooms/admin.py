from django.contrib import admin
from django.utils.html import mark_safe #<<<- admin security
from . import models

@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amentity)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display=(
        "name",
        "used_by"
    )

    def used_by(self,obj):
        return obj.rooms.count()

# another admin in admin
class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

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
        "count_photos",
        "total_rating",
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

    raw_id_fields = ("host",)

    search_fields = ("=city","^host__username")
    
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj): #self <- admin class obj <-now row
        return obj.amenities.count()

    def count_photos(self,obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition """

    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self,obj):
        return mark_safe(f'<img width="80px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"