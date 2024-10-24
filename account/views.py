from django.shortcuts import render, get_object_or_404, redirect
from django import views
from .models import Profile
from .forms import UserEditForm, ProfileEditForm, LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
# Create your views here.

class LoginView(views.View):

	def get(self, request, *args, **kwargs):

		form = LoginForm(request.POST or None)

		context = {
			'form' : form
		}

		return render(request, "login.html", context)

	def post(self, request, *args, **kwargs):

		form = LoginForm(request.POST or None)
		
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			
			if user:
				login(request, user)
				return HttpResponseRedirect('/')
		
		context = {
			'form' : form
		}

		return render(request, "login.html", context)


class RegistrationView(views.View):

	def get(self, request, *args, **kwargs):

		form = RegistrationForm(request.POST or None)

		context = {
			'form' : form
		}

		return render(request, "registration.html", context)

	def post(self, request, *args, **kwargs):

		form = RegistrationForm(request.POST or None)

		if form.is_valid():
			new_user = form.save(commit=False) #Не сохраняем в бд
			new_user.username = form.cleaned_data['username']
			new_user.email = form.cleaned_data['email']
			new_user.first_name = form.cleaned_data['first_name']
			new_user.last_name = form.cleaned_data['last_name']
			new_user.save()
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			# Customer.objects.create(
			# 	user=new_user,
			# 	phone=form.cleaned_data['phone'],
			# 	address=form.cleaned_data['address']
			# )
			Profile.objects.create(user=new_user)
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			return HttpResponseRedirect('/')

		context = {
			'form' : form
		}

		return render(request, "registration.html", context)


def AccountView(request):
	user = request.user
	profile = request.user.profile

	dic_obj = {
		'user' : user,
		'profile' : profile
	}

	return render(request, "account.html", dic_obj)

@login_required
def edit(request):
	user = request.user
	profile = request.user.profile

	if not hasattr(user, 'profile'):
		Profile.objects.create(user=user)

	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	dic_obj = {
		'user_form' : user_form,
		'profile_form' : profile_form,
		'user' : user,
		'profile' : profile
	}

	return render(request, 'account/edit.html', dic_obj)

