from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from attendance.prof.models import Attendance
from attendance.student.models import Attendance as StudentAttendance
from django.contrib.gis.geoip2 import GeoIP2
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
import random
import json

@csrf_exempt
@require_POST
def index(request):
    if request.method != 'GET' and request.method!='POST' :
        raise Exception
  
    code = random.randrange(0,9999)
    codestr = str(code).zfill(4)
    try:
        profIP = get_client_ip(request)
        g = GeoIP2()
        cityData = g.city(profIP)
    except:
        cityData = {'city':''}

    obj = Attendance.objects.create(class_code=codestr)

    json_data = json.loads(str(request.body,"utf-8"))

    try:
        obj.latitude = json_data['latitude']
        obj.longitude = json_data['longitude']
        obj.city = cityData['city']

    except KeyError:
        return HttpResponseBadRequest("Missing location data")  
    
    obj.save()
    
    returndict = {"code" : codestr, "latitude":str(obj.latitude), "longitude":str(obj.longitude)}
    return HttpResponse(json.dumps(returndict), content_type="application/json")

@csrf_exempt
@require_GET
def students(request):
    if request.method != 'GET':
        raise Exception
    code = request.GET.get('code','')
    if code=='':
        return HttpResponseBadRequest("Missing code data")
    ret_json={"num_of_students": StudentAttendance.objects.filter(code=code).count() }
    return HttpResponse(json.dumps(ret_json),content_type="application/json")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
