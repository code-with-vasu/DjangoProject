"""
URL configuration for P1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from A1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
path("accounts/", include("django.contrib.auth.urls")),
path('mailing-attach/', views.send_email_with_attachment),
path('mailing/', views.send_test_email),
path('register_patient/', views.register_patient),
path('patient_list/', views.patient_list),
path('register_doctor/', views.register_doctor),
path('appointment_list/', views.appointment_list),
path('doctors_list/', views.doctors_list),
path('doctor_schedule/', views.doctor_schedule),
path('assign_doctor/', views.assign_doctor),
path('billing_page/', views.billing_page),
path('payment_success/', views.payment_success),
path('create_checkout_session/<int:billing_id>/', views.create_checkout_session),
path('billing/invoice/<int:appointment_id>/', views.download_invoice, name='download_invoice'),
# Password Reset
#     path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
#     path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path("reset_done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
from django.contrib.auth import views as auth_views
from django.urls import path

