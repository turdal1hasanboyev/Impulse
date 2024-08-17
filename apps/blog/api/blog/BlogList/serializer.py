from rest_framework.serializers import ModelSerializer

from apps.blog.models import Blog
from apps.user.api.UserDetail.serializer import UserDetailSerializer


class BlogListSerializer(ModelSerializer):
    author = UserDetailSerializer(read_only=True)

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
