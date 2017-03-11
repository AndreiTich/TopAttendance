from django.shortcuts import render
from django.http import HttpResponse
from attendance.prof.models import Attendance
from django.views.decorators.http import require_POST
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
