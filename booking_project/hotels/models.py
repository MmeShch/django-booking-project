from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class Hotel(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    main_photo = models.ImageField(upload_to='hotels/', blank=True, null=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'hotels'
        ordering = ['name']


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='hotels/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo for {self.hotel.name}'



class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
        ('family', 'Family')
    ]

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms',
        db_column='hotel_id'
    )
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    main_photo = models.ImageField(upload_to='rooms/', blank=True, null=True)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'rooms'
        ordering = ['hotel', 'room_type']


    def __str__(self):
        return f"{self.hotel.name} - {self.get_room_type_display()} #{self.id}"


class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='rooms/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo for room {self.id} in {self.room.hotel.name}'
