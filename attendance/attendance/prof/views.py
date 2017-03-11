from django.shortcuts import render
from django.http import HttpResponse
from attendance.prof.models import Attendance
from django.views.decorators.csrf import csrf_exempt
import random
import json

@csrf_exempt
def index(request):
    if request.method != 'GET' and request.method!='POST' :
        raise Exception
  
    code = random.randrange(0,9999)
    codestr = str(code).zfill(4)
    obj = Attendance.objects.create(class_code=codestr)
    try:
        obj = Attendance.objects.get(id=1)
        obj.class_code = codestr
        obj.save()
    except Attendance.DoesNotExist:
        obj = Attendance.objects.create(class_code=codestr)

    if request.method == 'POST':
        json_data = json.loads(str(request.body,"utf-8"))
        try:
            obj.latitude = json_data['latitude']
            obj.longitude = json_data['longitude']
    
        except KeyError:
            return HttpResponseBadRequest("Missing location data")  
    
    obj.class_code = codestr
    obj.save()
    
    returndict = {"code" : codestr, "latitude":str(obj.latitude), "longitude":str(obj.longitude)}
    return HttpResponse(json.dumps(returndict), content_type="application/json")
