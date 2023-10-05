from django.urls import path

from robots.views import create_new_robot

urlpatterns = [
    path('new-robot/', create_new_robot, name='create_new_robot'),
]
