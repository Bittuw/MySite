from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import auth

from Conserts.forms import SigninForm


def singin(request):
	redirect = request.GET.get('continue', '/success')
	if request.method == "POST":
		form = SigninForm(request.POST)

		if form.is_valid():
			auth.login(request, form.cleaned_data['user'])
			return HttpResponseRedirect('singup')
	else:
		form = SigninForm()
	return render(request, 'index.html', {
        'form': form
    })

def main(request):
	return HttpResponse('singup/')

def singup(request):
	return HttpResponse('singup/')