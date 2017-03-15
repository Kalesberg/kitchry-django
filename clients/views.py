from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Client
import re
import random

# Create your views here.
def slugify(s):
	s = s.lower()

	for c in [' ', '-', '.', '/']:
		s = s.replace(c, '_')
	s = re.sub('\W', '', s)
	s = s.replace('_', ' ')
	s = re.sub('\s+', ' ', s)
	s = s.strip()
	s = s.replace(' ', '-')

	return s

def index(request):
	clients = Client.objects.all()
	return render(request,'clients/index.html',{'clients': clients})
	
def new(request):
	if(request.POST):
		s = slugify(request.POST['name'])
		if(_check(request.POST) == 1):
			return HttpResponse("Client with same name already exists!")
		elif(_check(request.POST) == 2):
			return HttpResponse("This email address already exists!")
		client = Client()
		client.name = request.POST['name']
		client.slug = s
		client.description = request.POST['description']
		client.email = request.POST['email']
		client.profile_img = request.POST['profile_img']
		client.weight = float(request.POST['weight'])
		client.stats = _stats(client.weight)		
		client.save()
		
		return HttpResponse("Client saved.")
	else:
		return render(request,'clients/new.html')
		
def client(request, alias):
	client = get_object_or_404(Client,slug = alias);
	if(request.POST):
		s = slugify(request.POST['name'])
		# if(_check(request.POST) == 1):
			# return HttpResponse("Client with same name already exists!")
		# elif(_check(request.POST) == 2):
			# return HttpResponse("This email address already exists!")		
		client.name = request.POST['name']
		client.slug = s
		client.description = request.POST['description']
		client.email = request.POST['email']
		client.profile_img = request.POST['profile_img']
		client.weight = float(request.POST['weight'])
		client.stats = _stats(client.weight)		
		client.save()
		
		return HttpResponseRedirect(reverse('clients:client', kwargs={'alias': s}))
	else:
		return render(request,'clients/client.html',{'client': client})
		
def _check(data):
	s = data['name']
	try:
		c = Client.objects.filter(name = s)
	except:
		c = None;
	if(c):
		return 1;
	s = slugify(data['name'])
	try:
		c = Client.objects.filter(slug = s)
	except:
		c = None;
	if(c):
		return 1;
		
	try:
		c = Client.objects.filter(email = data['email'])
	except:
		c = None;
	if(c):
		return 2;
		
def _stats(weight):
	w = []
	for x in range(52):
		w.append(round(random.uniform(weight - 10, weight + 10),1))
	ret = ',' . join(str(x) for x in w)
	return ret;
