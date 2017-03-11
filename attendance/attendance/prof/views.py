from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from attendance.prof.models import Attendance
from attendance.student.models import Attendance as StudentAttendance
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

    obj = Attendance.objects.create(class_code=codestr)

    json_data = json.loads(str(request.body,"utf-8"))

    try:
        obj.latitude = json_data['latitude']
        obj.longitude = json_data['longitude']

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

