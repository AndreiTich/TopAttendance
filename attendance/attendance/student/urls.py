from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'attendance-code/$', views.attendance_code),
]
