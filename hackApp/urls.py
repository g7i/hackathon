from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('problem',views.problem,name='problem'),
    path('prdesc',views.prdesc,name='prdesc'),
    path('idea/<int:pr>',views.idea,name='idea'),
    path('about',views.about,name='about'),
    path('past',views.past,name='past'),

    path('profile',views.profile,name='profile'),
]