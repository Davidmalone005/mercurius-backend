from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Name"),
    )

    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Email"),
    )

    message = models.TextField(
        null=False,
        blank=False,
        verbose_name=_("Message"),
    )

    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent At"))

    class Meta:
        ordering = ["-sent_at"]
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name
