# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse


# defining the function to convert an HTML file to a PDF file
import pdfkit
from django.template import context
from django.template.loader import get_template


def html_to_pdf(template_src, context_dict={}):
     # template = get_template(template_src)
     # html  = template.render(context_dict)
     # result = BytesIO()

     # pdf = pdfkit.from_file('test.html')
     body = """
         <html>
           <head>
             <meta name="pdfkit-page-size" content="Legal"/>
             <meta name="pdfkit-orientation" content="Landscape"/>
           </head>
           Hello World!
           </html>
         """
     # prepare your context for html template, like you do for django templates
     template = get_template('test.html')
     html = template.render(context=context)
     # return pdfkit.from_string(html)
     response = HttpResponse(pdfkit.from_string(html), content_type='application/pdf')
     return response