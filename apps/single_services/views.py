from django.shortcuts import render
from .models import *

def single_service1(request):
    serv1 = SingleService1.objects.latest('id')
    other_servs = OtherServs.objects.all()
    comments = Comments.objects.all()
    context = {
        'serv1': serv1,
        'comments': comments,
        'other_servs': other_servs,
    }
    return render(request, 'single_services/service-single1.html', context)


def single_service2(request):
    serv2 = SingleService2.objects.latest('id')
    plans = Plan.objects.all()
    comments = Comments.objects.all()
    contacts = Contacts.objects.latest('id')
    includes = Includes.objects.all()
    context = {
        'serv2': serv2, 
        'plans': plans,
        'comments': comments,
        'contacts':contacts,
        'includes': includes,
    }
    return render(request, 'single_services/service-single2.html', context)
