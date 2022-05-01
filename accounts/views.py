from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def user_login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    context = {'error': error}
    return render(request, 'accounts/login.html', context)
