from rest_framework.generics import ListAPIView

from apps.user.models import User
from .serializer import UsersListSerializer


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
