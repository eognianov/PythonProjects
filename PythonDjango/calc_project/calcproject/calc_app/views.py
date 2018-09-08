from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.
def add(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    data ={"result": arg1+arg2}
    result = json.dumps(data)
    return HttpResponse(result)


def multiply(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    data = {"result": arg1 * arg2}
    result = json.dumps(data)
    return HttpResponse(result)


def subtract(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    data = {"result": arg1 - arg2}
    result = json.dumps(data)
    return HttpResponse(result)


def divide(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    data = {"result": arg1 / arg2}
    result = json.dumps(data)
    return HttpResponse(result)
