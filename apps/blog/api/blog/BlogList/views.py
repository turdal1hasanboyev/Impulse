from rest_framework.generics import ListAPIView

from apps.blog.models import Blog
from apps.blog.api.blog.BlogList.serializer import BlogListSerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

    def get_queryset(self):
        return self.queryset.all().select_related("author")
    