from django.urls import path

from bookings.views import booking_views

urlpatterns = [
    path("", booking_views.BookingModelViewSet.as_view({"get": "list", "post": "create"})),
    path("<int:pk>", booking_views.BookingModelViewSet.as_view({"get": "retrieve", "put": "update"})),
]
