from django import forms
from django.contrib.auth import get_user_model
import re
from blog.models import Comment
from .models import Profile

User = get_user_model()

class UserEditForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields=['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['date_of_birth', 'photo']


class LoginForm(forms.ModelForm):
	"""Авторизация на сайте"""

	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		user = User.objects.filter(username=username).first()
		if not user:
			raise forms.ValidationError(f"Пользователь с логином {username} не найден в системе")
		if not user.check_password(password):
			raise forms.ValidationError('Неверный пароль')
		return self.cleaned_data

	class Meta:
		model = User
		fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
	"""Регистрация на сайте"""

	confirm_password = forms.CharField(widget=forms.PasswordInput)
	password = forms.CharField(widget=forms.PasswordInput)
	phone = forms.CharField(required=False) #реквард - поле не обязательно
	address = forms.CharField(required=False)
	email = forms.EmailField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'
		self.fields['confirm_password'].label = 'Подтвердите пароль'
		self.fields['phone'].label = 'Номер телефона'
		self.fields['address'].label = 'Адрес'
		self.fields['email'].label = 'Почта'
		self.fields['first_name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'

	def clean_email(self):
		email = self.cleaned_data['email']
		domain = email.split('.')[-1]
		if domain in ['net', 'xyz']:
			raise forms.ValidationError(f"Регистрация для домена {domain} невозможна.")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError(f"Данный почтовый адрес уже зарегистрирован.")
		return email

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError(f"Имя {username} занято. Попробуйте другое.")
		if not re.match("^[a-zA-Z0-9@.+-_]+$", username):
			raise forms.ValidationError("Имя пользователя может содержать только латинские буквы, цифры и символы @/./+/-/_ .")
		return username

	def clean(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']
		if password != confirm_password:
			raise forms.ValidationError("Пароли не совпадают.")
		return self.cleaned_data

	class Meta:
		model = User
		fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'phone', 'address', 'email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']