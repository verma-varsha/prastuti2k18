from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, LoginForm

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #print("form valid")
            userObj = form.cleaned_data
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            username = userObj['email']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user1 = User.objects.create_user(username, email, password)
                user1.first_name = first_name
                user1.last_name = last_name
                user1.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like an account with that email already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form' : form})

def login_view(request):
    error=""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['email']
            password = userObj['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # Todo: check up if the email is in database or not and then give error message accordingly 
                error = "Sorry. That login was invalid. Try again!"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form, 'error': error})