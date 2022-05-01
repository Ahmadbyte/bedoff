import pdfkit
from django.http import HttpResponse
from django.template import loader
from filters.mixins import FiltersMixin
from rest_framework import filters

from base.views import BaseAPIView, BaseModelViewSet
from bookings import models as booking_models
from bookings.serializers import booking_serializers


class BookingModelViewSet(FiltersMixin, BaseModelViewSet):
    """
    BookingModelViewSet
    """

    lookup_field = "uid"
    serializer_class = booking_serializers.BookingModelSerializer
    filter_backends = (filters.OrderingFilter,)
    queryset = booking_models.Booking.objects.all().order_by("-created_at")


class DownloadBookingVoucherAPIView(BaseAPIView):
    """
    DownloadBookingVoucherAPIView
    """

    voucher_pdf = "booking_voucher.html"

    def html_to_pdf(self, voucher_context: dict):
        """
        html_to_pdf
        """
        html = loader.render_to_string(self.voucher_pdf, voucher_context)
        output = pdfkit.from_string(html, output_path=False)
        response = HttpResponse(content_type="application/pdf")
        response.write(output)
        return response

    def _get_guest_list(self, booking_obj):
        """
        _get_guest_list
        """
        guest_list = ""
        for guest in booking_obj.guests.all():
            guest_list = guest_list.join(f"{guest.first_name} {guest.last_name}")
        return guest_list

    def compute_context_for_rendering_voucher(self, booking_obj):
        """
        compute_data_for_rendering_voucher
        """
        return {
            "guest_list": self._get_guest_list(booking_obj),
        }

    def get(self, request, *args, **kwargs):
        """
        get
        """
        booking_uid = kwargs.get("booking_id")
        booking_obj = booking_models.Booking.objects.filter(uid=booking_uid).first()
        context = self.compute_context_for_rendering_voucher(booking_obj)
        return self.html_to_pdf(voucher_context=context)
