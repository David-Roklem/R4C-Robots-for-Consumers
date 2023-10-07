from django.urls import path

from robots.views import create_new_robot, generate_report_view

urlpatterns = [
    path('new-robot/', create_new_robot, name='create_new_robot'),
    path('download-report/', generate_report_view, name='download_report'),
]
