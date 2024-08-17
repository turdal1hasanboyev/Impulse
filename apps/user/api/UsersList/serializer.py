from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UsersListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            "username",
            "email",
            "first_name",
            "last_name",
            "description",
            "profile_photo",
            "phone_number",
            "created_at",
        ]
