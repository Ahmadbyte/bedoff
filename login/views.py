from django.shortcuts import render
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action , api_view, schema
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
# @schema(CustomAutoSchema())
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})