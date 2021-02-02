from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        print('creating form')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            print('form not valid!')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')