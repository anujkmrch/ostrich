# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Light, Status,Camera, Density

admin.site.register(Light)
admin.site.register(Status)
admin.site.register(Camera)
admin.site.register(Density)

# Register your models here.