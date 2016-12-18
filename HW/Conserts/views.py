from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def singin(request):
	return HttpResponse('singin')

def main(request):
	return HttpResponseRedirect('singin/')

def singup(request):
	return HttpResponse('sinup')