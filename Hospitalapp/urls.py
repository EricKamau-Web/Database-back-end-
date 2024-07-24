
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('Doctors/', views.Doctors, name='Doctors'),
    path('appointment/', views.Appointments, name='appointments'),

]
