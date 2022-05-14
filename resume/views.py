from django.shortcuts import render
from .models import Profile,Skill
# Create your views here.


def myResume(request):
    profiles = Profile.objects.all()
    skills = Skill.objects.all()
    context ={
        'profile':profiles,'skills':skills
    }
    return render(request,'resume/profile.html',context)
