from django.shortcuts import render,render_to_response
import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def index(requet):
	task_list = list(models.Task.objects.all())
	task_list.sort(cmp=None, key=lambda x:x.deadline)
	print task_list
	return render_to_response('index.html', locals() )

