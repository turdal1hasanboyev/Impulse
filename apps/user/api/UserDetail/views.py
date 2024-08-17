from rest_framework.generics import RetrieveAPIView

from apps.user.models import User

from apps.user.api.UserDetail.serializer import UserDetailSerializer


class UserDetaliView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'
