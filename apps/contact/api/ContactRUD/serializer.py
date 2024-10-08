from rest_framework.serializers import ModelSerializer

from apps.contact.models import Contact


class ContactRUDSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            "name",
            "email",
            "message",
            "created_at",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
