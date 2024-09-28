# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# def members(request):
#   template = loader.get_template('mytemplate.html')
#   context = { 'points':5,}
#   return HttpResponse(template.render(context, request))


def perro(request):
    return HttpResponse("Hello world!")