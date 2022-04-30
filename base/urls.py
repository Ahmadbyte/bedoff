from django.urls import path

from base import views as base_views

urlpatterns = [
    path("meta", base_views.MetaDataAPIView.as_view(), name="metadata_api"),
]
