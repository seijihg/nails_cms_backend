from django.urls import path

from bookings.views_api import MakeBooking

app_name = "bookings"

urlpatterns = [
    path(
        "v1/make-booking/",
        MakeBooking.as_view(),
        name="make-booking-api",
    ),
]
