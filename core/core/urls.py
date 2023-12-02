from django.contrib import admin
from django.urls import path

import django.conf import from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
