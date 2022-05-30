import pdfkit
from django.http import HttpResponse
from django.template import loader
from url_filter.integrations.drf import DjangoFilterBackend

from base.views import BaseAPIView, BaseModelViewSet
from bookings import models as booking_models
from bookings.serializers import booking_serializers


class BookingModelViewSet(BaseModelViewSet):
    """
    BookingModelViewSet
    """

    lookup_field = "uid"
    serializer_class = booking_serializers.BookingModelSerializer
    queryset = booking_models.Booking.objects.all().order_by("-created_at")
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "booking_status",
    ]

    def get_serializer_class(self):
        """
        get_serializer_class
        """
        if self.request.method == "PUT":
            return booking_serializers.UpdateBookingModelSerializer
        return booking_serializers.BookingModelSerializer


class DownloadBookingVoucherAPIView(BaseAPIView):
    """
    DownloadBookingVoucherAPIView
    """

    cancelled_voucher_pdf = "cancelled-voucher.html"
    confirmed_voucher_pdf = "confirmed-voucher.html"

    def generate_pdf_voucher_from_template(self, voucher_context: dict, booking_obj):
        """
        html_to_pdf
        """
        if booking_obj.booking_status == booking_models.Booking.COMPLETED:
            boooking_voucher_template = self.confirmed_voucher_pdf
        else:
            boooking_voucher_template = self.cancelled_voucher_pdf

        html = loader.render_to_string(boooking_voucher_template, voucher_context)
        output = pdfkit.from_string(html, output_path=False)
        response = HttpResponse(content_type="application/pdf")
        response.write(output)
        response["Content-Disposition"] = "attachment; filename=%s.pdf" % str(booking_obj.uid)
        return response

    def _get_guest_list(self, booking_obj):
        """
        _get_guest_list
        """
        guest_list = ""
        for guest in booking_obj.guests.all():
            guest_name = f"{guest.first_name}, "
            if guest.last_name:
                guest_name = f"{guest.first_name} {guest.last_name}, "
            guest_list = guest_list + guest_name
        guest_list = guest_list.strip().strip(",")
        return guest_list

    def _get_day_from_date(self, booking_obj):
        """
        _get_day_from_date
        """
        day_list = ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]
        date = day_list[booking_obj.check_in.weekday()] + "day"
        return date

    def _get_hotel_address(self, hotel_obj):
        """
        _get_hotel_address
        """
        address_obj = hotel_obj.hotel_address
        return f"""{address_obj.name}, {address_obj.address1}, {address_obj.address2},
                   {address_obj.zip_code}, {address_obj.city}, {address_obj.state},
                   {address_obj.country}""".strip().strip(
            ","
        )

    def compute_context_for_rendering_voucher(self, booking_obj):
        """
        compute_data_for_rendering_voucher
        """
        return {
            "guest_list": self._get_guest_list(booking_obj),
            "booking_date": f"{booking_obj.created_at:%B %d, %Y}",
            "booking_id": booking_obj.uid,
            "hotel_name": booking_obj.hotel.name,
            "hotel_location_link": booking_obj.hotel.hotel_address.map_url,
            "checkin_date": f"{booking_obj.check_in:%B %d, %Y}",
            "checkout_date": f"{booking_obj.check_out:%B %d, %Y}",
            "guest_count": len(booking_obj.guests.all()),
            "checkin_day": self._get_day_from_date(booking_obj),
            "checkout_day": self._get_day_from_date(booking_obj),
            "checkin_nights_count": (booking_obj.check_out - booking_obj.check_in).days,
            "room_count": booking_obj.single_occupancy_room_count + booking_obj.double_occupancy_room_count,
            "single_occupancy_room_count": booking_obj.single_occupancy_room_count,
            "double_occupancy_room_count": booking_obj.double_occupancy_room_count,
            "hotel_address": self._get_hotel_address(booking_obj.hotel),
        }

    def get(self, request, *args, **kwargs):
        """
        get
        """
        booking_uid = kwargs.get("booking_id")
        booking_obj = booking_models.Booking.objects.filter(uid=booking_uid).first()
        context = self.compute_context_for_rendering_voucher(booking_obj)
        return self.generate_pdf_voucher_from_template(voucher_context=context, booking_obj=booking_obj)
