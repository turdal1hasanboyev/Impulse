from django.db import models

from apps.common.models import baseModel

from ckeditor.fields import RichTextField


class Contact(baseModel):
    name = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(null=True, blank=True, unique=True, max_length=225)
    message = RichTextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    