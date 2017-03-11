import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from attendance.student.models import Attendance
from attendance.prof.models import Attendance as ProfAttendance
from math import cos, asin, sqrt


@require_POST
@csrf_exempt
def attendance_code(request):
    json_data = json.loads(str(request.body,"utf-8"))
    try:
        student_id = json_data['student_id']
        code = json_data['code']
        latitude = float(json_data['latitude'])
        longitude = float(json_data['longitude'])
    except KeyError:
        return HttpResponseBadRequest()

    if not student_id.isdigit():
        return HttpResponseBadRequest("Student id must be numbers only!")
    if len(code) != 4:
        return HttpResponseBadRequest("Code must be 4 digits!") 
    if not ProfAttendance.objects.filter(class_code=code).exists():
        return HttpResponseBadRequest("Class code does not exist!") 
    #need to add validation for geo location here
    prof_latitude = float(ProfAttendance.objects.get(class_code=code).latitude)
    prof_longitude = float(ProfAttendance.objects.get(class_code=code).longitude)

    if distance(prof_latitude, prof_longitude, latitude, longitude) > 100:
        return HttpResponseBadRequest("You might be in a wrong classroom.") 

    s = Attendance(student_id=student_id, code=code, latitude=latitude, longitude=longitude)
    s.save()

    return HttpResponse("student_id: {}, code: {}, latitude: {}, longitude: {}".format(student_id, code, latitude, longitude))


#in meters
def distance(prof_latitude, prof_longitude, student_latitude, student_longitude):
    degToRadFactor = 0.017453292519943295
    haversineDistance = 0.5 - cos((student_latitude - prof_latitude) * p)/2 + cos(prof_latitude * p) * cos(student_latitude * p) * (1 - cos((student_longitude - prof_longitude) * p)) / 2
    diameterEarth = 12742
    return float(diameterEarth * asin(sqrt(a)) * 1000)

