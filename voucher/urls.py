from django.urls import path

from voucher import views

urlpatterns = [
    path("pdf", views.create_pdf()),
]
