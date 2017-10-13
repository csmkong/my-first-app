from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid

# Create your views here.
def home(request):
	return HttpResponse("Hello "+request.META['REMOTE_ADDR'])

def ip(request):
	jsonContext = {}
	jsonContext['origin'] = request.META['REMOTE_ADDR']
	context = json.dumps(jsonContext)
	return HttpResponse(context)

def uuid_view(request):
	jsonContext = {}
	jsonContext['uuid'] = str(uuid.uuid4())
	context = json.dumps(jsonContext)
	return HttpResponse(context)

def user_agent(request):
	jsonContext = {}
	jsonContext['user-agent'] = request.META['HTTP_USER_AGENT']
	context = json.dumps(jsonContext)
	return HttpResponse(context)
