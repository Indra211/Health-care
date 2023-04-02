from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class new_user(AbstractUser):
    phone = models.CharField(max_length=15)
    
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    contact = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(new_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.title

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(new_user, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    reason = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.date} {self.time} {self.doctor.name}'
