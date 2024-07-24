from django.shortcuts import render,redirect
from Hospitalapp.models import Appointment

# Create your views here.
def index(request):
    return render(request,'index.html')

def inner(request):
    return render(request,'inner-page.html')

def about(request):
    return render(request,'about.html')

def Doctors(request):
    return render(request,'Doctors.html')

def Appointments(request):
    if request.method == 'POST':
        Appointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            doctor = request.POST['doctor'],
            department= request.POST['department'],
            message = request.POST['message'],

        )
        Appointments.save()
        return redirect("/appointment")

    else:
        return render(request,'appointment.html')
def services(request):
    return render(request,'services.html')