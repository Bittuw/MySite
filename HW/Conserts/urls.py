from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'main$', views.main , name = 'main'),
	url(r'signin', views.signin, name = 'signin'),
	url(r'signup$', views.signup, name = 'signup'),
	url(r'logout$', views.logout, name = 'logout'),
	url(r'main_list/(?P<page_id>[0-9]*)$', views.MainList.as_view(), name = 'main_list'),
	url(r'consert/(?P<pk>[0-9]+)', views.ConsertView.as_view(), name = 'consert'),
	# url(r'$', views.main, name = 'main'),
]