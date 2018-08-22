from django.http import HttpResponse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from . models import *

# Create your views here.

def index(request):
    if 'user_id' in request.session:
        return redirect('/home')
    return render(request, 'home/index.html')
def signup(request, *args, **kwargs):
    return render(request, 'home/signup.html')

def login(request, *args, **kwargs):
    return render(request, 'home/login.html')

def register_process(request, *args, **kwargs):
    postData = {
		'first_name': request.POST['first_name'],
		'last_name': request.POST['last_name'],
        'gender': request.POST['gender'],
        'age': request.POST['age'],
		'email': request.POST['email'],
		'password': request.POST['password'],
		'conf_password': request.POST['conf_password'],
	}
    if not User.objects.register_validator(postData):
        # add user to database
        new_user_id = User.objects.create_user(postData)
        request.session['user_id'] = new_user_id
        print('im in!')
        return redirect('/home')

    for error in User.objects.register_validator(postData):
        messages.error(request, error)
    return redirect('/sign_up')


def login_process(request, *args, **kwargs):

    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/login')
    request.session['user_id'] = result.id
    return redirect('/home')
# @login_required
def home(request, *args, **kwargs):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'home/success.html')
# @login_required
def logout(request):
    context = {
        "logout" : request.session.pop("user_id")
    }
    return render(request, "home/index.html", context)
