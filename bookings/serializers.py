from django.db import transaction
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField
from django.core.exceptions import ValidationError

from bookings.models import Booking

import arrow


class MakeBookingSerializer(serializers.ModelSerializer):
    time_zone = TimeZoneSerializerField()

    class Meta:
        model = Booking
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)

    def validate(self, attrs):
        date_time = attrs.get("date_time")
        time_zone = attrs.get("time_zone")
        print(date_time)
        booking_time = arrow.get(date_time, time_zone)

        if booking_time < arrow.utcnow():
            raise ValidationError(
                "You cannot schedule an appointment for the past. "
                "Please check your time and time_zone"
            )
