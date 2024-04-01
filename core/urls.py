from django.contrib import admin
from django.urls import path

from calculator import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("calculator/", views.view1, name="list")
]
