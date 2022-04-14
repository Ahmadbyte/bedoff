# from rest_framework import status
# from rest_framework.decorators import api_view, parser_classes
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
#
# # Create your views here.
# # from hotels.DTO_serializer.req_objects import HotelFilterSerializer
#
#
# @api_view(["GET", "POST"])
# @parser_classes([JSONParser])
# def hotels(request):
#     # if request.method == "POST":
#     # add filter logic
#     # filterSerializer = HotelFilterSerializer(data=request.data)
#     # if filterSerializer.is_valid():
#     # Hotel.objects.all()
#     # resultSerializerdata = BookingGroupSerializer(a, many=True)
#     # content = JSONRenderer().render(resultSerializerdata.data)
#     # HotelList = []
#     # for itr in len(bg):
#     #     bgi = BookingGroupRes()
#     #     bookingGroupList.append(bgi)
#
#     # return Response(HotelList, status=status.HTTP_200_OK)
#
#     return Response(status=status.HTTP_400_BAD_REQUEST)
