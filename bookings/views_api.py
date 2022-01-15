from rest_framework.permissions import IsAuthenticated
from bookings import serializers
from rest_framework import generics


class MakeBooking(generics.CreateAPIView):
    serializer_class = serializers.MakeBookingSerializer
    permission_classes = [IsAuthenticated]
