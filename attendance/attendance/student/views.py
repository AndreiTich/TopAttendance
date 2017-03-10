import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from attendance.student.models import Attendance


@require_POST
@csrf_exempt
def attendance_code(request):
    json_data = json.loads(request.body)
    try:
        student_id = json_data['student_id']
        code = json_data['code']
    except KeyError:
        return HttpResponseBadRequest()
        
    if not student_id.isdigit():
        return HttpResponseBadRequest("Student id must be numbers only!")
    if len(code) != 4:
        return HttpResponseBadRequest("Code must be 4 digits!")    

    s = Attendance(student_id=student_id, code=code)
    s.save()

    return HttpResponse("student_id: {}, code: {}".format(student_id, code))



