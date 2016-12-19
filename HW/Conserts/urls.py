from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'singup$', views.singup, name = 'singup'),
	url(r'$', views.singin, name = 'main' ),
	
	#url(r'logout$', views.logout, name = 'logout'),
	#url(r'success$', views.success, name = 'success'),
	#url(r'Conserts$', Conserts.as_view(), name = 'Conserts'),
	#url(r'Consert$', Consert.as_view(), name = 'Consert'),
	#url(r'AddConsert$', AddConsert.as_view(), name = 'AddConsert'),
]