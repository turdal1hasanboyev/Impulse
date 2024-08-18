from rest_framework.generics import CreateAPIView

from apps.user.models import User
from .serializer import UserCreateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
