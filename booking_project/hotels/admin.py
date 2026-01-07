from django.contrib import admin
from hotels.models import Hotel, Room, Review, HotelPhoto, RoomPhoto


class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1


class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['name', 'location']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [HotelPhotoInline]

    def is_active(self, obj):
        return not obj.is_deleted
    is_active.boolean = True


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price_per_night', 'is_available']
    list_filter = ['room_type', 'is_available', 'hotel']
    list_editable = ['is_available']
    inlines = [RoomPhotoInline]
    list_select_related = ['hotel']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'hotel')
    search_fields = ('hotel__name', 'user__username')





