from django.db import models
from django.core.exceptions import ValidationError
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser

import arrow


class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    mobile_phone_number = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class Address(TimeStampedModel):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=50)

    users = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        return f"Post Code: {self.postcode}"

    def clean(self):
        """Checks that appointments are not scheduled in the past"""
        appointment_time = arrow.get(self.time, self.time_zone.zone)

        if appointment_time < arrow.utcnow():
            raise ValidationError(
                "You cannot schedule an appointment for the past. "
                "Please check your time and time_zone"
            )
