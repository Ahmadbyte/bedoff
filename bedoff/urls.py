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

import bms.models
import hotel.models
import login.apps

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r"^user(?P<id>.+)$", login.models.user),
    # re_path(r"^user$", login.apps.LoginConfig),
    # re_path(r"^guestsByIds$", login.apps.LoginConfig),
    re_path(r"^OrderUpload$", bms.models.BookingOrder),
    re_path(r"^Hotel$", hotel.models.Hotel),
    re_path(r"^BookingsByIds$", bms.models.Booking ),
    re_path(r"^Bookings$", bms.models.Booking),
    re_path(r"^Booking$", bms.models.Booking),
]
