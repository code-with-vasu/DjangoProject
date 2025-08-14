from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Billing
from django.http import HttpResponse


def generate_invoice(request, appointment_id):
    billing = Billing.objects.get(appointment_id=appointment_id)
    html_string = render_to_string('A1/invoice_template.html', {'billing': billing})

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{appointment_id}.pdf"'
    return response