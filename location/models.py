from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    location_address = models.TextField()
    loc_x_coor = models.CharField(max_length=10)
    loc_y_coor = models.CharField(max_length=10)
    def __str__(self):
        return self.location_name
