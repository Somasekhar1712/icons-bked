from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('search/', views.search.as_view(), name='search'),
    path("icons/", views.icons.as_view(), name="icons"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
