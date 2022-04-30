from django.shortcuts import render

# Create your views here.
from voucher.service.process import html_to_pdf


def create_pdf(request):

    return html_to_pdf()
