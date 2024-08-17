from rest_framework.serializers import ModelSerializer

from apps.blog.models import Blog


class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
            "author",
            "created_at",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
