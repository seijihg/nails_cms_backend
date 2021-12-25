from django.urls import path
from users.views_api import UserList

app_name = "users"


urlpatterns = [
    path(
        "v1/users/",
        UserList.as_view(),
        name="users-api",
    )
]
