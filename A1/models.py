from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.TextField()
    phone = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Appointment: {self.patient.name} with {self.doctor.name} on {self.date}"


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
        ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day} ({self.start_time} - {self.end_time})"


class Billing(models.Model):
    appointment = models.OneToOneField('Appointment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Invoice for {self.appointment} - {self.status}"
