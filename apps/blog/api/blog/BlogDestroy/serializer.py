from rest_framework.serializers import ModelSerializer

from apps.blog.models import Blog


class BlogDestroySerializer(ModelSerializer):
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
