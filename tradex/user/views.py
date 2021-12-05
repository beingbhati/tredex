# from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from user.forms import LoginForm, RegisterForm
from user.models import MyUser
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register_request(request):

  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      new_user.set_password(form.cleaned_data['password'])
      messages.success(request, "Registration successful.")
      new_user.save()
  else:
      form = RegisterForm()
      messages.error(request, "Unsuccessful registration. Invalid information.")
  return render(request, 'register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            # user = get_object_or_404(MyUser, username = username)
            # print(user.email)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request, "YOur're Logged in successful")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request, "login.html", {'form': form})

