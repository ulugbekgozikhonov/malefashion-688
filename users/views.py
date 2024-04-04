from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView
from products.models import WishlistModel


# Create your views here.

class SignUpView(CreateView):
	form_class = UserCreationForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('users:signin')


def sign_up(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		password_confirm = request.POST.get('password_confirm')
		if password == password_confirm:
			user = User.objects.filter(username=username).exists()
			if user:
				return HttpResponse('User already exists !')
			else:
				user = User.objects.create_user(username=username, password=password)
				login(request, user)
				return redirect('pages:home')
		else:
			return HttpResponse("Password don't match !")
	return render(request, template_name="registration/signup.html")


class SignInView(FormView):
	form_class = AuthenticationForm
	template_name = 'registration/signin.html'
	success_url = reverse_lazy('pages:home')


def sign_in(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('pages:home')
		else:
			return redirect('users:signin')
	return render(request, template_name="registration/signin.html")


def sign_out(request):
	logout(request)
	return redirect('pages:home')


class WishListView(ListView):
	template_name = 'wishlist.html'
	model = WishlistModel
	context_object_name = 'wishlists'

	def get_queryset(self):
		return WishlistModel.objects.filter(user=self.request.user)
