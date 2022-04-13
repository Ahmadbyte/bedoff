from base.serializers import BaseModelSerializer
from bookings import models as booking_models


class BookingModelSerializer(BaseModelSerializer):
    """
    BookingModelSerializer
    """

    class Meta:
        model = booking_models.Booking
        fields = "__all__"
