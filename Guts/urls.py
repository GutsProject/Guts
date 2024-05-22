
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("reperguts/", include("reperguts.urls")),
    path("admin/", admin.site.urls)
]
