from rest_framework.generics import ListCreateAPIView

from apps.blog.models import travelImages
from apps.blog.api.travelimages.TravelImagesLC.serializer import TravelImagesLCSerializer

class TravelImagesLCView(ListCreateAPIView):
    queryset = travelImages.objects.all()
    serializer_class = TravelImagesLCSerializer
