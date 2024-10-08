from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.contact.models import Contact
from .serializer import ContactRUDSerializer


class ContactRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactRUDSerializer
    lookup_field = "pk"
