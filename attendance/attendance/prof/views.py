from django.shortcuts import render
from django.http import HttpResponse
import random
import json

def index(request):
    if request.method == 'GET':
        code = random.randrange(0,9999)
        codestr = str(code).zfill(4)
        returndict = {"code" : codestr}
        return HttpResponse(json.dumps(returndict), content_type="application/json")


# Create your views here.
