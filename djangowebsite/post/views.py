# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# def index(request):

# 	return render(request, 'post/index.html')
	
def login(request):
    return render(request, 'post/login.html')
    	
def test(request):
	return render(request, 'post/test.html')

def connectdb(request):
	return render(request, 'post/connectdb.html')
