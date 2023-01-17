from weakref import proxy
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class hospital(models.Model):
    hos_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.hos_name


class doctor(models.Model):
    name = models.CharField(max_length=100)
    depart = models.CharField(max_length=100)
    degree = models.TextField(max_length=500)
    date = models.CharField(max_length=100)
    hos_name = models.ForeignKey(
        hospital, on_delete=models.CASCADE, db_column="hos_name"
    )

    def __str__(self):
        return self.name


class appointment(models.Model):
    date = models.CharField(max_length=10)
    time = models.CharField(blank=True, max_length=10)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="Pending")
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.name + " ---- " + self.patient.username
