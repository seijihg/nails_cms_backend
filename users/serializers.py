from rest_framework import serializers
from users.models import User
from django.core.validators import RegexValidator

from home.regex import PHONE_NUMBER_REGEX_SIGNUP

phone_uk_regex = RegexValidator(
    regex=PHONE_NUMBER_REGEX_SIGNUP, message="Please enter a valid UK telephone number."
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    mobile_phone_number = serializers.CharField(
        validators=[phone_uk_regex], allow_blank=False
    )
