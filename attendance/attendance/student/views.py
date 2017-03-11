import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from attendance.student.models import Attendance
from attendance.prof.models import Attendance as ProfAttendance


@require_POST
@csrf_exempt
def attendance_code(request):
    json_data = json.loads(request.body)
    try:
        student_id = json_data['student_id']
        code = json_data['code']
        latitude = json_data['latitude']
        longitude = json_data['longitude']
    except KeyError:
        return HttpResponseBadRequest()

    if not student_id.isdigit():
        return HttpResponseBadRequest("Student id must be numbers only!")
    if len(code) != 4:
        return HttpResponseBadRequest("Code must be 4 digits!") 
    if not ProfAttendance.objects.filter(class_code=code).exists():
        return HttpResponseBadRequest("ClassCode does not exist!") 
    #need to add validation for geo location here

    s = Attendance(student_id=student_id, code=code, latitude=latitude, longitude=longitude)
    s.save()

    return HttpResponse("student_id: {}, code: {}, latitude: {}, longitude: {}".format(student_id, code, latitude, longitude))



