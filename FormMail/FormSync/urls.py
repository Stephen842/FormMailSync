from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('message_sent/', views.message_sent, name='message_sent'),
]