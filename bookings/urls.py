from django.urls import path

from bookings.views import booking_views

urlpatterns = [
    path("", booking_views.BookingModelViewSet.as_view({"get": "list", "post": "create"}), name="list_bookings"),
    path(
        "<uuid:uid>",
        booking_views.BookingModelViewSet.as_view({"get": "retrieve", "put": "update"}),
        name="fetch_booking_details",
    ),
    path(
        "voucher/<uuid:booking_id>",
        booking_views.DownloadBookingVoucherAPIView.as_view(),
        name="download_booking_voucher",
    ),
]
