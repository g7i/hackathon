from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('signups',views.signups,name='signups'),
    path('signupm',views.signupm,name='signupm'),
    path('signupj',views.signupj,name='signupj'),
    path('signupp',views.signupp,name='signupp'),
    url(r'^login/$',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('aadhar', views.aadhar, name='aadhar'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]