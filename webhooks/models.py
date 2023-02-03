from django.db import models
from django.urls import reverse

# Create your models here.


class Webhook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    