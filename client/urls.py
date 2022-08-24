from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Register/$',Register,name="Register"),
	# url(r'^Login/$',Login,name="Login"),
]