import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geoip2 import GeoIP2
from attendance.student.models import Attendance
from attendance.prof.models import Attendance as ProfAttendance
from math import cos, asin, sqrt


@require_POST
@csrf_exempt
def attendance_code(request):
    json_data = json.loads(str(request.body,"utf-8"))
    requestIP = get_client_ip(request)
    try:
        g = GeoIP2()
        cityData = g.city(requestIP)
        student_city = cityData['city']
    except: 
        student_city = ''

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
    if not ProfAttendance.objects.last().class_code == code:
        return HttpResponseBadRequest("Incorrect class code!") 
    if Attendance.objects.filter(student_id=student_id, code=code).exists():
        return HttpResponseBadRequest("Attendance already submitted")
        
    #need to add validation for geo location here
    prof_latitude = float(ProfAttendance.objects.get(class_code=code).latitude)
    prof_longitude = float(ProfAttendance.objects.get(class_code=code).longitude)
    prof_city = str(ProfAttendance.objects.get(class_code=code).city)

    if distance(prof_latitude, prof_longitude, latitude, longitude) > 50 and ( student_city == prof_city or student_city == '' ):
        return HttpResponseBadRequest("You might be in a wrong classroom and/or city.") 

    s = Attendance(student_id=student_id, code=code, latitude=latitude, longitude=longitude)
    s.save()

    return HttpResponse("student_id: {}, code: {}, latitude: {}, longitude: {}".format(student_id, code, latitude, longitude))

#in meters
def distance(prof_latitude, prof_longitude, student_latitude, student_longitude):
    degToRadFactor = 0.017453292519943295
    haversineDistance = 0.5 - cos((student_latitude - prof_latitude) * degToRadFactor)/2 + cos(prof_latitude * degToRadFactor) * cos(student_latitude * degToRadFactor) * (1 - cos((student_longitude - prof_longitude) * degToRadFactor)) / 2
    diameterEarth = 12742
    return float(diameterEarth * asin(sqrt(haversineDistance)) * 1000)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
