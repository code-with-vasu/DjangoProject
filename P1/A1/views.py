
# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import *


def register_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']

        Doctor.objects.create(name=name, specialization=specialization, phone=phone, email=email)
        return redirect('/doctors_list')
    return render(request, 'A1/register1.html')

def doctors_list(request):
    doctors_list1=Doctor.objects.all()
    return render(request,'A1/doctors_list.html',{'doctors_list1':doctors_list1})

def register_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        medical_history = request.POST['medical_history']

        Patient.objects.create(name=name, age=age, gender=gender, address=address, phone=phone, medical_history=medical_history)
        return redirect('patient_list')

    return render(request, 'A1/register.html')

def patient_list(request):
    patient_list1=Patient.objects.all()
    return render(request,'A1/patient_list.html',{'patient_list1':patient_list1})



def appointment_list(request):
    appointment_list1=Appointment.objects.all()
    return render(request,'A1/appointment_list.html',{'appointment_list1':appointment_list1})

def doctor_schedule(request):
    doctor_schedule_list1=DoctorSchedule.objects.all()
    return render(request,'A1/doctor_schedule.html',{'doctor_schedule_list1':doctor_schedule_list1})

#
from datetime import datetime
def assign_doctor(request):
    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']

        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(patient=patient, doctor=doctor,date='2000-01-01',time='12:25', status='Pending')

        return redirect('/appointment_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'A1/assign_doctor.html', {'patients': patients, 'doctors': doctors})


from .models import Billing
from .utils import generate_invoice

def billing_page(request):
    bills = Billing.objects.all()
    return render(request, 'A1/billing_list.html', {'bills': bills})

def download_invoice(request, appointment_id):
    return generate_invoice(request, appointment_id)



# this is all about Payemtn related

import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Billing

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, billing_id):
    billing = get_object_or_404(Billing, id=billing_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': f"Appointment with {billing.appointment.doctor}"},
                'unit_amount': int(billing.amount * 100),  # Convert dollars to cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/payment/success/') + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri('/payment/cancel/'),
    )

    billing.stripe_payment_id = session.id
    billing.save()

    return JsonResponse({'sessionId': session.id})


def payment_success(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)

    billing = Billing.objects.get(stripe_payment_id=session.id)
    billing.status = 'Paid'
    billing.save()

    return render(request, 'A1/payment_success.html')


def payment_cancel(request):
    return render(request, 'payment_cancel.html')
