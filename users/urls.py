from django.urls import path
from users.views_api import UserDetails, UserList

app_name = "users"


urlpatterns = [
    path(
        "v1/users/",
        UserList.as_view(),
        name="users-list-api",
    ),
    path(
        "v1/users/<int:pk>/",
        UserDetails.as_view(),
        name="users-details-api",
    ),
]
