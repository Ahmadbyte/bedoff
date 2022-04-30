from django.shortcuts import render

# Create your views here.
import pdfkit
from django.http import HttpResponse
from django.template import loader

def create_pdf():
    html = loader.render_to_string('test.html', {})
    output= pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response
