from django.contrib import admin
from hotels.models import Hotel, Room

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'rating', 'created_at']
    list_display_links = ['name', 'location']
    list_filter = ['rating', 'deleted']
    search_fields = ['name', 'location']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'get_room_type_display', 'price_per_night', 'available']
    list_display_links = ['hotel', 'get_room_type_display']
    list_filter = ['room_type', 'available', 'hotel__location', 'deleted']
    search_fields = ['hotel__name']



