from rest_framework.generics import UpdateAPIView

from apps.blog.models import Blog
from apps.blog.api.blog.BlogUpdate.serializer import BlogUpdateSerializer


class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogUpdateSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.all().select_related("author")
    