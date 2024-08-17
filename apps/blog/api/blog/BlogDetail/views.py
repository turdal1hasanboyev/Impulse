from rest_framework.generics import RetrieveAPIView

from apps.blog.models import Blog
from apps.blog.api.blog.BlogDetail.serializer import BlogDetailSerializer


class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.all().select_related("author")
    