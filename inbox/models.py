from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class Inbox(models.Model):
    admin = models.ForeignKey(
        User,
        default=1,
        verbose_name=_("Admin"),
        related_name="from_admin",
        on_delete=models.DO_NOTHING,
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("Customer"),
        related_name="to_customer",
        on_delete=models.CASCADE,
    )

    subject = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Subject"),
    )

    message = models.TextField(
        null=False,
        blank=False,
        verbose_name=_("Message"),
    )

    has_been_read = models.BooleanField(
        default=False, verbose_name="Has Been Read"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At")
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Inbox")
        verbose_name_plural = _("Inbox")

    def __str__(self):
        return self.subject
