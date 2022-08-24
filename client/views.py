from django.shortcuts import render
from .models import Client, Wallet_Client

def Register(request):
	if request.method == 'POST':
		Client(
			name = request.POST.get('name'),
			phone = request.POST.get('phone'),
			email = request.POST.get('email'),
			user = request.POST.get('username'),
			password = request.POST.get('pswd')
		).save()
		Wallet_Client(
			amount = 0,
			client = Client.objects.get(email = request.POST.get('email'))
		).save()
		request.session['email_client'] = request.POST.get('email') 

	return render(request,'authentication/register_client.html')