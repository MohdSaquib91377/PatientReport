from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.conf import settings
from .models import Patient
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def authenticate_patient(email, password):
    try:
        patient = Patient.objects.get(email=email)
    except Patient.DoesNotExist:
        return None
    else:
        if patient.check_password(password):
            return patient
    return None

def login_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email and password is not None:
            patient=authenticate_patient(email,password)
            print('authenticate')
            if patient:
                print('yes')
                login(request,patient)
                return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL))
            else:
                messages.error(request, 'Incorrect email or password') 
        else:
            pass
    return render(request, 'patient/signin.html', {})
    