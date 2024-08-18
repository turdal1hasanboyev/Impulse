from rest_framework.generics import CreateAPIView

from apps.blog.models import Blog
from .serializer import BlogCreateSerializer


class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
