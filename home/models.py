# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_number = models.CharField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Devices(models.Model):

    #__Devices_FIELDS__
    device_type = models.TextField(max_length=255, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)

    #__Devices_FIELDS__END

    class Meta:
        verbose_name        = _("Devices")
        verbose_name_plural = _("Devices")



#__MODELS__END
