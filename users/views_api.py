from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from users import serializers
from users.models import User
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = []

    def list(self, request, format=None):
        queryset = self.get_queryset()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            User.objects.get(email__iexact=request.data.get("email"))
        except ObjectDoesNotExist:
            request.data["username"] = request.data.get("email")
            response = super().create(request, *args, **kwargs)
            return response
        return Response(status=status.HTTP_409_CONFLICT)
