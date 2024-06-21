
from django.urls import path
from room import views

app_name = 'room'

urlpatterns = [
    path('room/', views.room, name='room'),

]

