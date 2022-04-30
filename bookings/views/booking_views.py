from filters.mixins import FiltersMixin
from rest_framework import filters

from base.views import BaseModelViewSet
from bookings import models as booking_models
from bookings.serializers import booking_serializers


class BookingModelViewSet(FiltersMixin, BaseModelViewSet):
    """
    BookingModelViewSet
    """

    lookup_field = "uid"
    serializer_class = booking_serializers.BookingModelSerializer
    filter_backends = (filters.OrderingFilter,)
    queryset = booking_models.Booking.objects.all()
