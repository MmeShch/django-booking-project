<<<<<<< HEAD
# from django.db import models
#
# class Hotel(models.Model):
#     name = models.CharField(max_length=250)
#     location = models.CharField(max_length=200)
#     description = models.TextField()
#     photos = models.ImageField(upload_to='hotels/', blank=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     deleted = models.BooleanField(default=False)
=======
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=200)
    description = models.TextField()
    photos = models.ImageField(upload_to='hotels/', blank=True)
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
        


    def __str__(self):
        return self.name



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
    photos = models.ImageField(upload_to='rooms/', blank=True)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'rooms'


    def __str__(self):
        return f"{self.hotel.name} - {self.get_room_type_display()} #{self.id}"
>>>>>>> feat/hotels-app
