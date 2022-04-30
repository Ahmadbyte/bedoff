
from django.http import HttpResponse


# defining the function to convert an HTML file to a PDF file
import pdfkit
from django.template import loader


def html_to_pdf():
     html = loader.render_to_string('test.html', {})
     output = pdfkit.from_string(html, output_path=False)
     response = HttpResponse(content_type="application/pdf")
     response.write(output)
     return response

def fill_data():
     pass
