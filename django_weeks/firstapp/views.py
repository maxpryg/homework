from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import date


def hellodjango(response):
    return HttpResponse('Hello Django!')


def greeting(response, name):
    return HttpResponse(f'Hello {name}!')


def fulldate(response):
    full_date = date.today().strftime('%d.%m.%Y')
    return HttpResponse(full_date)


def year(response):
    return HttpResponse(date.today().year)


def day(response):
    day = date.today().strftime('%d')
    return HttpResponse(day)


def month(response):
    month = date.today().strftime('%m')
    return HttpResponse(month)


@api_view()
def hello_world(request):
    return Response({'msg': 'Hello, world!'})


@api_view()
def today(request):
    full_date = date.today().strftime('%d/%m/%Y')
    year = date.today().year
    month = date.today().strftime('%m')
    day = date.today().strftime('%d')

    return Response({'date': full_date,
                     'year': year,
                     'month': month,
                     'day': day
                     })


@api_view()
def my_name(request):
    name_of_hacker = request.query_params.get('name_of_hacker')
    if not name_of_hacker:
        return Response(
            {'error': 'Wrong parameter. Need param <name_of_hacker>'})
    return Response({'name': name_of_hacker})


@api_view(['POST'])
def calculator(request):
    actions = {'plus': lambda x, y: x + y,
               'minus': lambda x, y: x - y,
               'multiply': lambda x, y: x * y,
               'divide': lambda x, y: x / y
               }

    action = request.data.get('action')
    number1 = request.data.get('number1')
    number2 = request.data.get('number2')

    if action not in actions.keys():
        return Response({'error':
                         f'Bad action value. Acceptable values are: '
                         f'{", ".join(key for key in actions.keys())}'})

    if number2 == 0:
        return Response({'error': 'Division by zero.'})

    result = actions[action](number1, number2)

    return Response({'result': result})
