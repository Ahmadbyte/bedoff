from django.urls import path

from hotels.views import hotel_views

urlpatterns = [path("", hotel_views.HotelsModelViewSet.as_view({"get": "list", "post": "create"})),
               path("<int:pk>", hotel_views.HotelsModelViewSet.as_view({"get": "retrieve", "put": "update"}))]

