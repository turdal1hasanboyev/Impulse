from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.models import travelImages
from .serializer import TravelImagesRUDSerializer

class TravelImagesRUDView(RetrieveUpdateDestroyAPIView):
    queryset = travelImages.objects.all()
    serializer_class = TravelImagesRUDSerializer
    lookup_field = "pk"
