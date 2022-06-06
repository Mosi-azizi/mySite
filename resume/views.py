from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import http

from .models import Profile
from settings.models import StieSetting
from .forms import MessageFrom
from .signals import send_welcomeMail

# Create your views here.


def myResume(request):
    profile = Profile.objects.first()
    siteSetting = StieSetting.objects.first()
    messageForm = MessageFrom()
    if request.method == 'POST':
        form = MessageFrom(request.POST)
        if form.is_valid():
            message_income = form.save(commit=False)

            try:
                send_welcomeMail(siteSetting.welcomeMessage_sub,siteSetting.welcomeMessage_body,message_income.email)
            except:
                print("Welcome email could not send! ")
                pass
            message_income.save()
            # messages.success(request, 'Your message successfully sent!')
            return redirect(myResume)

    context ={
        'profile':profile,'messageForm':messageForm,'siteSetting':siteSetting
    }
    return render(request,'resume/profile.html',context)
