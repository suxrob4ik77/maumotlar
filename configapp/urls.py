
from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index,name='Home' ),
    path('add_news/',add_news,name='add_news'),
    path('add_cat/',add_news,name='add_cat'),
    path('about_news/<int:new_id>/', about_news, name='about_news'),
    path('',loginPage,name='login' ),

]

