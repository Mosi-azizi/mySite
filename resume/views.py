from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import  login,authenticate,logout
from django.contrib.auth.models import User


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
            messages.success(request, 'Your message successfully sent!')
            return redirect('resume:myresume')


    context ={
        'profile':profile,'messageForm':messageForm,'siteSetting':siteSetting
    }
    return render(request,'resume/profile.html',context)


def loginUser(request):
    # page = 'login'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username'].lower()
        password = request.POST['password']
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     # print('Username dose not exist!')
        #     messages.error(request, 'Username dose not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, ' Please check Username or Password !')
    context ={}
    return render(request, 'login/login-register.html', context)


def adminPanel(request):
    return redirect('/admin/')

def logoutUser(request):
    logout(request)
    return redirect('/')