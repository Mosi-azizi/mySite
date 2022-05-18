from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import http

from .models import Profile,Skill
from .forms import MessageFrom
# Create your views here.


def myResume(request):
    # profiles = Profile.objects.all()
    profile = Profile.objects.get(username__iexact='sa_azizi')
    skills = Skill.objects.all()
    messageForm = MessageFrom()
    if request.method == 'POST':
        messageForm = MessageFrom(request.POST)
        if messageForm.is_valid():
            messageForm.save()
            return redirect(myResume)
            messages.success(request,'Your message successfully sent!')


    context ={
        'profile':profile,'skills':skills,'form':messageForm
    }
    return render(request,'resume/profile.html',context)
