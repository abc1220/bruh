from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Location

# Create your views here.

def index(request):
    all_locations=Location.objects.all()
    template = loader.get_template('location/index.html')
    context = {
        'all_locations': all_locations,
    }
    return HttpResponse(template.render(context, request))

