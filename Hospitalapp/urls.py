
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='home'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('Doctors/', views.Doctors, name='Doctors'),
    path('appointment/', views.Appointments, name='appointments'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete,),
    path('patient/', views.patient,name = 'patient'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),

]
