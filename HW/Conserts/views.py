from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.views import View
from django.contrib import auth

from Conserts.forms import SigninForm, SignupForm
from Conserts.models import Consert

def main(request):
	return render(request, 'main.html')


def signin(request):
	redirect = request.GET.get('continue', 'main')

	if request.user.is_authenticated:
		return HttpResponseRedirect(redirect)

	if request.method == "POST":
		form = SigninForm(request.POST)

		if form.is_valid():
			auth.login(request, form.cleaned_data['user'])
			return HttpResponseRedirect(redirect)
	else:
		form = SigninForm()
	return render(request, 'signin.html', {
        'form': form,
        'redirect' : redirect,
    })


def signup(request):
	redirect = request.GET.get('continue', 'main')
	if request.user.is_authenticated():
		return HttpResponseRedirect(redirect)

	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			return HttpResponseRedirect(redirect)
	else:
		form = SignupForm()

	return render(request, 'signup.html', {
        'form': form,
        'redirect': redirect,
	})


def logout(request):
    redirect = request.GET.get('continue', 'main')
    auth.logout(request)
    return HttpResponseRedirect(redirect)

class main_list(ListView):

	context_object_name = "Conserts"
	queryset = Consert.objects.all()
	template_name = "main_list.html"

	def get(self, request):
		if not request.is_ajax():
			return ListView.get(self, request)
		else:
			pass

