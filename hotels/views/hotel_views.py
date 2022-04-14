from base.views import BaseModelViewSet
from hotels import models as hotel_models
from hotels.serializers import hotel_serializers


class HotelsModelViewSet(BaseModelViewSet):
    """
    HotelsModelViewSet
    """

    queryset = hotel_models.Hotel.objects.all()
    serializer_class = hotel_serializers.HotelModelSerializer
