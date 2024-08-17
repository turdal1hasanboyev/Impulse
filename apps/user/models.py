from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.common.models import baseModel


class User(baseModel, AbstractUser):
    description = RichTextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profilePhotos/", null=True, blank=True)
    phone_number = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.get_full_name()}"
    