import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt
def attendance_code(request):
    json_data = json.loads(request.body)
    try:
        student_id = json_data['student_id']
        code = json_data['code']
    except KeyError:
        return HttpResponseBadRequest()

    return HttpResponse("student_id: {}, code: {}".format(student_id, code))

# Create your views here.
