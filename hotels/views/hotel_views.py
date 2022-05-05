from url_filter.integrations.drf import DjangoFilterBackend

from base.views import BaseModelViewSet
from hotels import models as hotel_models
from hotels.serializers import hotel_serializers


class HotelsModelViewSet(BaseModelViewSet):
    """
    HotelsModelViewSet
    """

    lookup_field = "uid"
    queryset = hotel_models.Hotel.objects.all().order_by("-created_at")
    serializer_class = hotel_serializers.HotelModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "name",
    ]
