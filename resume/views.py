from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import http

from .models import Profile,Skill,Education,Employment,Message
from settings.models import StieSetting
from .forms import MessageFrom
from .signals import send_welcomeMail

# Create your views here.

subject = 'Thanks From Sam'
message = 'Dear sir/madam' \
          'I am very happy you flow me'
def myResume(request):
    profile = Profile.objects.first()
    siteSetting = StieSetting.objects.first()
    messageForm = MessageFrom()
    if request.method == 'POST':
        form = MessageFrom(request.POST)
        if form.is_valid():
            message_income = form.save(commit=False)
            # print(message_income.email)
            send_welcomeMail(subject, message, message_income.email)
            message_income.save()
            messages.success(request, 'Your message successfully sent!')
            return redirect(myResume)

    context ={
        'profile':profile,'messageForm':messageForm,'siteSetting':siteSetting
    }
    return render(request,'resume/profile.html',context)
