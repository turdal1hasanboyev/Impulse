from django.db import models

import uuid

from django.template.defaultfilters import slugify 
from django.urls import reverse

from ckeditor.fields import RichTextField

from apps.common.models import baseModel
from apps.user.models import User


class Blog(baseModel):
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="blogPhotos/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"
    

class travelImages(baseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="travelImages/", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
