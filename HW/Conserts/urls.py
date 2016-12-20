from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'main$', views.main , name = 'main'),
	url(r'signin$', views.signin, name = 'signin' ),
	url(r'signup$', views.signup, name = 'signup'),
	url(r'logout$', views.logout, name = 'logout'),
	#url(r'main_list$', main_list.as_view(), name = 'main_list')
	
]