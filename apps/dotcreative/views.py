from django.shortcuts import render
from .models import *

def homepage(request):
    slides = Slides.objects.latest('id')
    block1 = Block1.objects.latest('id')
    category = CategoryPortfolio.objects.all()
    services = Services.objects.all()
    adverts = Advertisement.objects.latest('id')
    reviews = Reviews.objects.all()
    contacts = Contacts.objects.latest('id')
    portfols = Portfolio.objects.all()
    context = {
        'slides': slides,
        'block1': block1,
        'category': category,
        'services': services,
        'adverts': adverts,
        'reviews': reviews,
        'contacts': contacts,
        'portfols': portfols,
    }
    return render(request, 'index.html', context)


def about(request):
    about = About.objects.latest('id')
    context = {
        'about': about
    }
    return render(request, 'about/about.html', context) 


def projects(request):
    portfols = Portfolio.objects.all()
    context = {
        'portfols': portfols,
    }
    return render(request, 'about/projects.html', context)

def blog_page(request):
    posts_recent = Posts.objects.filter(tag = 'recent')
    posts_others = Posts.objects.filter(tag = 'others')
    context = {
        'posts_others': posts_others,
        'posts_recent': posts_recent,
    }
    return render(request, 'about/blog.html', context)

def contacts(request):
    contacts = Contacts.objects.latest('id')
    context = {
        'contacts': contacts,
    }
    return render(request, 'about/contact.html', context)