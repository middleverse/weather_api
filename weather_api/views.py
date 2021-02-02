from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        print('creating form')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            form.save()
            return redirect('/')
        else:
            print('form not valid!')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form })