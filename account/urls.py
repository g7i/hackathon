from django.urls import path,include
from . import views

urlpatterns = [
    path('signups',views.signups,name='signups'),
    path('signupm',views.signupm,name='signupm'),
    path('signupj',views.signupj,name='signupj'),
    path('signupp',views.signupp,name='signupp'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('aadhar',views.aadhar,name='aadhar'),
]