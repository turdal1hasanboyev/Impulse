from rest_framework.generics import DestroyAPIView

from apps.user.models import User
from .serializer import UserDeleteSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    lookup_field = "pk"
