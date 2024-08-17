from rest_framework.generics import DestroyAPIView

from apps.blog.models import Blog
from apps.blog.api.blog.BlogDestroy.serializer import BlogDestroySerializer


class BlogDestroyView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDestroySerializer
    lookup_field = "slug"
    