from rest_framework.generics import ListCreateAPIView

from apps.contact.models import Contact
from .serializer import ContactLCSerializer


class ContactLCView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactLCSerializer
