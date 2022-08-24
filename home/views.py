from django.http import HttpResponse
from django.shortcuts import render,redirect
from model.models import Modelo
from study.models import Study
from client.models import *
from model.models import Modelo, Wallet_Model

def Home(request):
	return render(request,'index.html')


def Register(request):
	mssg = ""
	if request.method == 'POST':
		if request.POST.get('term') is not None:
			try:
				Study(
					name_study = request.POST.get('username'),
					pswd = request.POST.get('pswd'),
					email = request.POST.get('email'),
					birthday = request.POST.get('birthday')
				).save()
				return redirect('Home')
			except Exception as e:
				mssg = "Ese nombre ya esta registrado"
	return render(request,'authentication/register.html',{'mssg':mssg})

def Login(request):
	if request.method == 'POST':
		try:
			study = Study.objects.get(email = request.POST.get('email'), pswd= request.POST.get('pswd'))
			
			return redirect('Home')
		except Study.DoesNotExist as e:
			print("Error")
	return render(request,'authentication/login.html')


def Shopping_Tokens(request):
	if request.is_ajax():
		c = Client.objects.get(email = request.session['email_client'])
		wallet = Wallet_Client.objects.get(client=c)
		wallet.amount = wallet + int(request.GET.get('dollar'))
		wallet.save()
		return HttpResponse(wallet.convert_dollar_to_tokens())


def Dar_Tips(request):
	if request.is_ajax():
		c = Client.objects.get(email = request.session['email_client'])
		wallet = Wallet_Client.objects.get(client=c)
		if wallet.convert_dollar_to_tokens() > 0:
			w = Wallet_Model.objects.last()
			w.amount = w.amount + int(request.GET.get('tips'))
			w.save()
		return HttpResponse()



