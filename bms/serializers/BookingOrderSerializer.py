from rest_framework_json_api import serializers

from bms.models import BookingOrder, Vendor


class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = ('id','name')
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=50)

class BookingOrderSerializer(serializers.Serializer):
    # class Meta:
    #     model = BookingOrder
    #     fields = ('id' , 'vendor' , 'ordered_on' , 'source')
    id = serializers.IntegerField()
    vendor=VendorSerializer()
    ordered_on=serializers.DateTimeField()
    source=serializers.CharField()

