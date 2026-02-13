from django.contrib import admin
from django.urls import path, include
from django.conf import settings

print("ALLOWED_HOSTS:", settings.ALLOWED_HOSTS)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
