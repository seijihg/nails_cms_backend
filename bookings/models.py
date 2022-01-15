from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import User
from timezone_field import TimeZoneField


class Booking(TimeStampedModel):
    services = models.JSONField(blank=True, default=dict)
    date_time = models.DateTimeField()
    time_zone = TimeZoneField(default="UTC")

    booked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="booked_by"
    )
    done_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="done_by"
    )
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="customer"
    )

    def __str__(self):
        return (
            f"Done by: {self.done_by} for {self.customer}. Time Slot: {self.date_time} "
        )
