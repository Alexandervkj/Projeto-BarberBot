from django.urls import path
from . import views

urlpatterns = [
    path('agendamento/', views.appointment_view, name='appointment'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]
