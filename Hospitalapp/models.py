from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()


    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()
    appointments = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.fullname