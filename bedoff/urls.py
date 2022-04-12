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
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

import accounts.views
import bookings.views
import hotels.views

schema_view = get_swagger_view(title="Pastebin API")

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^$", schema_view),
    re_path(r"^User(?P<id>.+)$", accounts.views.view),
    re_path(r"^User$", accounts.views.view),
    re_path(r"^Hotels/Hotel$", hotels.views.hotels),
    re_path(r"^Hotels$", hotels.views.hotels),
    re_path(r"^Bookings/Booking$", bookings.views.booking),
    re_path(r"^Bookings$", bookings.views.booking_groups),
    re_path(r"^Bookings/Order$", bookings.views.order),
    re_path(r"^Booking/Guest", bookings.views.guest),
]
