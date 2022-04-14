from base.views import BaseModelViewSet
from bookings import models as booking_models
from bookings.serializers import booking_serializers


class BookingModelViewSet(BaseModelViewSet):
    """
    BookingModelViewSet
    """

    queryset = booking_models.Booking.objects.all()
    serializer_class = booking_serializers.BookingModelSerializer


class BookingListModelViewSet(BaseModelViewSet):
    """
    BookingModelViewSet
    """

    queryset = booking_models.Booking.objects.all()
    serializer_class = booking_serializers.BookingsModelSerializer
