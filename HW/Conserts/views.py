from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views import View
from django.contrib import auth
from django.conf import settings
import os
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from Conserts.forms import SigninForm, SignupForm, ConsertForm
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

        return render(request, 'sign_errors.html', {'form': form})

    else:
        form = SigninForm()
    return render(request, 'signin.html', {
        'form': form,
        'redirect': redirect,
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
            return JsonResponse({'error': 'False', 'redirect': redirect})
        return JsonResponse({'error': 'True', 'errors': form.errors})
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


class MainList(ListView):

    context_object_name = "Conserts"
    template_name = "main_list.html"

    def get(self, request, page_id):

        objects_on_list = 3
        page_id = int(page_id) if page_id else 0
        start = len(Consert.objects.all())
        tmp = start - objects_on_list * page_id
        start = tmp if tmp > 0 else 0

        to = start - objects_on_list
        to = to if to > 0 else 0
        self.queryset = Consert.objects.all()[to: start: -1]
        return ListView.get(self, request)

    def get_context_data(self, **kwargs):
        context = super(MainList, self).get_context_data(**kwargs)
        context['form'] = ConsertForm()
        return context

    def post(self, request, page_id):
        form = ConsertForm(request.POST, request.FILES)

        if not form.is_valid():
            return JsonResponse(form.errors)

        consert = form.fill_object()
        f = request.FILES.get('image')

        if f is not None:
            img_url = r'image/%s.jpg' % (consert.id)
            FileSystemStorage().save(
                os.path.join(
                    settings.MEDIA_ROOT,
                    img_url),
                File(f)
                )
            consert.image = img_url
            consert.save()
        return HttpResponseRedirect('consert/%d' % (consert.id,))


class ConsertView(DetailView):
    model = Consert
    template_name = "consert_detail.html"
    context_object_name = "consert"

    @method_decorator(login_required)
    def get(self, request, pk):
        cur_consert = Consert.objects.get(id=int(pk))
        return render(
            request,
            'consert_detail.html',
            {
                'consert': cur_consert,
                'reservation': cur_consert.reservation.all(),
                'status': cur_consert.reservation.filter(
                    id=request.user.id).exists(),
            }
        )
        # return DetailView.get(self, request)

    def post(self, request, pk):
        cur_consert = Consert.objects.get(id=int(pk))
        user = request.user
        state = request.POST.get('state', 'False')
        is_reservated = cur_consert.reservation.filter(id=user.id).exists()
        if state == 'True' and not is_reservated:
            cur_consert.reservation.add(user)

        if state == 'False' and is_reservated:
            cur_consert.reservation.remove(user)

        return render(request, 'users.html', {
            'consert': cur_consert,
            'reservation': cur_consert.reservation.all()
            })
