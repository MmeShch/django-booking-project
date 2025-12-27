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
