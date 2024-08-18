from django.urls import path

from .api.ContactLC.views import ContactLCView
from .api.ContactRUD.views import ContactRUDView


app_name = "contact"

urlpatterns = [
    path('contactlc/', ContactLCView.as_view(), name='contactlc'),
    path('contactrud/<int:pk>/', ContactRUDView.as_view(), name='contactrud'),
]
