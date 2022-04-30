from django.urls import path

from voucher import views

urlpatterns = [
    path("", views.create_pdf),
]
