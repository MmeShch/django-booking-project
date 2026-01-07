from rest_framework import serializers
from .models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer):
    room_type_name = serializers.CharField(source='get_room_type_display', read_only=True)

    class Meta:
        model = Room
        fields = [
            'id',
            'room_type',
            'room_type_name',
            'price_per_night',
            'is_available',
            'main_photo'
        ]


class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    rooms_count = serializers.SerializerMethodField()
    photo_count = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'slug',
            'location',
            'description',
            'rating',
            'rooms',
            'rooms_count',
            'photo_count'
        ]

    def get_rooms_count(self, obj):
        return obj.rooms.filter(deleted=False).count()

    def get_photo_count(self, obj):
        return obj.photos.count()