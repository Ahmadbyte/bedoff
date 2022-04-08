"""bedoff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view

import bms.views
import hotel.views
import login.views

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', schema_view),
    re_path(r"^User(?P<id>.+)$", login.views.view),
    re_path(r"^User$", login.views.view),
    re_path(r"^Hotels/Hotel$", hotel.views.hotels),
    re_path(r"^Hotels/$", hotel.views.hotels),
    re_path(r"^Bookings/Booking$", bms.views.booking),
    re_path(r"^Bookings$", bms.views.booking_groups),
    re_path(r"^Bookings/Order$", bms.views.order),
    re_path(r"^Booking/Guest", bms.views.guest),
]
