from django.shortcuts import render
from django.http import HttpResponse
from attendance.prof.models import Attendance
import random
import json

def index(request):
    if request.method != 'GET':
        raise Exception

    code = random.randrange(0,9999)
    codestr = str(code).zfill(4)

    try:
        obj = Attendance.objects.get(id=1)
        obj.class_code = codestr
        obj.save()
    except Attendance.DoesNotExist:
        Attendance.objects.create(class_code=codestr)

    returndict = {"code" : codestr}
    return HttpResponse(json.dumps(returndict), content_type="application/json")



# Create your views here.
