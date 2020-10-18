from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed

from django.views.decorators.csrf import ensure_csrf_cookie

NUMBERS = {'A': 1234,
           'B': 4567}

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def num_add(request, *args, **kwargs):
    result = NUMBERS.get('A') + NUMBERS.get('B')
    print(result)
    answer = {
        'answer': result
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def num_subtract(request, *args, **kwargs):
    result = NUMBERS.get('A') - NUMBERS.get('B')
    print(result)
    answer = {
        'answer': result
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def num_multiply(request, *args, **kwargs):
    result = NUMBERS.get('A') * NUMBERS.get('B')
    print(result)
    answer = {
        'answer': result
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


def num_divide(request, *args, **kwargs):
    result = NUMBERS.get('A') / NUMBERS.get('B')
    print(result)
    answer = {
        'answer': result
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response

