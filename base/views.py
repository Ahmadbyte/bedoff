from rest_framework import status as http_status_codes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from bookings import models as booking_models
from hotels import models as hotel_models


class BaseModelViewSet(ModelViewSet):
    pass


class BaseAPIView(APIView):
    pass


class MetaDataAPIView(BaseAPIView):
    """
    MetaDataAPIView
    """

    def get(self, request, *args, **kwargs):
        """
        get
        """
        response_data = {
            "booking_type_choices": [{"key": k[0], "value": k[1]} for k in booking_models.Booking.BOOKING_TYPE_CHOICES],
            "booking_stay_type_choices": [
                {"key": k[0], "value": k[1]} for k in booking_models.Booking.BOOKING_STAY_TYPE_CHOICES
            ],
            "booking_status_choices": [
                {"key": k[0], "value": k[1]} for k in booking_models.Booking.BOOKING_TYPE_CHOICES
            ],
            "hotel_staff_type_choices": [
                {"key": k[0], "value": k[1]} for k in hotel_models.HotelStaff.STAFF_TYPE_CHOICES
            ],
        }
        return Response(data=response_data, status=http_status_codes.HTTP_200_OK)
