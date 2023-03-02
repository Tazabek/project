from django.shortcuts import render
from .models import *

def service1(request):
    category = CategoryPortfolio.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'services/services1.html', context)

def service2(request):
    service2 = Service2.objects.all()
    context = {
        'service2': service2
    }
    return render(request, 'services/services2.html', context)

def service3(request):
    service3 = Service3.objects.all()
    plans = Plan.objects.all()
    includes = Includes.objects.all()
    context = {
        'service3': service3,
        'plans_of': plans,
        'includes': includes,
    }
    return render(request, 'services/services3.html', context)

def service4(request):
    service3 = Service3.objects.all()
    context = {
        'service3': service3,
    }
    return render(request, 'services/services4.html', context)

def service5(request):
    service5 = Service5.objects.all()
    includes5 = IncludesServ.objects.all()
    context = {
        'service5': service5,
        'include5': includes5,
    }
    return render(request, 'services/services5.html', context)

