from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'attendance-code/$', views.index, name='index'),
]