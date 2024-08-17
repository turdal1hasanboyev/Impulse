from rest_framework.generics import CreateAPIView

from apps.user.models import User
from apps.user.api.UserCreate.serializer import UserCreateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
