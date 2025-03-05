from django.contrib import admin

# Register your models here.
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','address','phone','medical_history']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','specialization','phone','email','availability']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','date','time','status']

class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ['doctor','day','start_time','end_time']

class BillingAdmin(admin.ModelAdmin):
    list_display = ['appointment','amount','status','created_at']




admin.site.register(Billing,BillingAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(DoctorSchedule,DoctorScheduleAdmin)
# dashboard custamaiztion

admin.site.site_header = "Hospital Management Admin"
admin.site.site_title = "Hospital Admin Portal"
admin.site.index_title = "Welcome to the Hospital Management Dashboard"
