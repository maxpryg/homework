from django.http import HttpResponse

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
