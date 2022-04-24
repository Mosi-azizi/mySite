from django.shortcuts import render

# Create your views here.
def myResume(request):
    context ={

    }
    return render(request,'resume/profile.html',context)
