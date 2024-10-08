from rest_framework.generics import UpdateAPIView

from apps.user.models import User
from .serializer import UserUpdateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'pk'
