from django.db import models

# Create your models here.

class products(models.Model):
    product_name = models.CharField(max_length = 100)
    product_type = models.CharField(max_length = 100)
    product_owner = models.CharField(max_length = 100)

    def __str__(self):
        return self.product_name

class user(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    mobile = models.IntegerField()
    place = models.CharField(max_length = 100)
    user_type = models.IntegerField()
    password = models.CharField(max_length = 100,default = ' ')

    def __str__(self):
        return self.name


class user_types(models.Model):
    name = models.CharField(max_length = 100)
    user_type = models.IntegerField()

    def __str__(self):
        return self.name


class bookings(models.Model):
    user = models.CharField(max_length = 100)
    booking_date = models.DateField(auto_now=True)
    booking_place = models.CharField(max_length = 100)
    booking_receiver = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.user


