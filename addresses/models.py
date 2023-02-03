from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.

class Address(models.Model):
  user = models.ForeignKey(User, verbose_name=_("User"),
        related_name="user",
        on_delete=models.PROTECT,)
  
  house_no = models.CharField(max_length=5, null=False, blank=False, unique=False, verbose_name=_("House Number"))

  street_name = models.CharField(max_length=500, null=False, blank=False, unique=False, verbose_name=_("Street Name"))

  bus_stop = models.CharField(max_length=60, null=False, blank=False, unique=False, verbose_name=_("Nearest Bus Stop"))

  lga = models.CharField(max_length=60, null=False, blank=False, unique=False, verbose_name=_("LGA"))

  postal_code = models.IntegerField(default=0, null=True, blank=True, unique=False, verbose_name=_("LGA Postal Code"))

  state = models.CharField(max_length=60, null=False, blank=False, unique=False, verbose_name=_("State"))

  country = models.CharField(max_length=60, default="Nigeria", null=False, blank=False, unique=False, verbose_name=_("Country"))

  is_default = models.BooleanField(default=False)

  added_on = models.DateTimeField(auto_now_add=True)

  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-added_on"]
    verbose_name = _("Address")
    verbose_name_plural = _("Addresses")
  
  def __str__(self):
    return self.user.fullname