from django.urls import path
from . import views

app_name='resume'
urlpatterns =[
   path('',views.myResume, name='myresume'),
   path('login/',views.loginUser, name='login'),
   path('logout/',views.logoutUser, name='logout'),
   path('adminPannel/',views.adminPanel, name='adminPanel')

]