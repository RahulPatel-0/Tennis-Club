from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def main(request):
  template=loader.get_template('main.html')
  return HttpResponse(template.render())
  
  

def members(request):
  mymembers=Member.objects.all()
  template=loader.get_template('all_members.html')
  context={
    'mymembers':mymembers,
  }
  return HttpResponse(template.render(context,request))


def details(request,id):
  mymembers=Member.objects.get(id=id)
  template=loader.get_template('details.html')
  context={
    'mymembers':mymembers,
  }
  return HttpResponse(template.render(context,request))

def testing(request):
  template=loader.get_template('template.html')
  context={
    'fruits':['Apple','Banana','Cherry'],
  }
  return HttpResponse(template.render(context,request))