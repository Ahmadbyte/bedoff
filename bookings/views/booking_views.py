from filters.mixins import (FiltersMixin,)
from rest_framework import filters

from base.views import BaseModelViewSet
from bookings import models as booking_models
from bookings.serializers import booking_serializers
from bookings.validations.BookingQuerySchema import bookings_query_schema


class BookingModelViewSet(FiltersMixin, BaseModelViewSet):
    """
    BookingModelViewSet
    """

    # queryset = booking_models.Booking.objects.all()
    serializer_class = booking_serializers.BookingModelSerializer
    filter_backends = (filters.OrderingFilter,)

    filter_validation_schema = bookings_query_schema


    def get_queryset(self):
        """
               Optionally restricts the queryset by filtering against
               query parameters in the URL.
        """

        query_params = self.request.query_params

        url_params = self.kwargs

        # get queryset_filters from FilterMixin
        queryset_filters = self.get_db_filters(url_params, query_params)

        # This dict will hold filter kwargs to pass in to Django ORM calls.
        db_filters = queryset_filters['db_filters']

        db_excludes = queryset_filters['db_excludes']

        queryset = booking_models.Booking.objects.all()
        status = self.request.query_params.get('status')

        # return queryset.filter(**db_filters).exclude(**db_excludes)
        return queryset.filter(status=status)




class BookingListModelViewSet(BaseModelViewSet):
    """
    BookingModelViewSet
    """

    queryset = booking_models.Booking.objects.all()
    serializer_class = booking_serializers.BookingsModelSerializer
