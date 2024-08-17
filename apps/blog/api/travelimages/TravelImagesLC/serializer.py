from rest_framework.serializers import ModelSerializer

from apps.blog.models import travelImages


class TravelImagesLCSerializer(ModelSerializer):
    class Meta:
        model = travelImages
        fields = [
            'id',
            "name",
            "image",
            "created_at",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
