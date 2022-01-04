from rest_framework.response import Response
from users import serializers
from users.models import User
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = []

    def list(self, request, format=None):
        queryset = self.get_queryset()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetails(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
