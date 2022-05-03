from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
from base.models import Applicant, Blog, Contact, Event, Post


def home(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        try:
            Contact.objects.create(
                name=name, subject=subject, email=email, message=message)
            error = 'no'
        except:
            error = 'yes'
    blogs = Blog.objects.order_by('-id')[0:3]
    posts = Post.objects.order_by('-id')[0:3]
    events = Event.objects.order_by('-id')[0:3]
    x = {'error': error, 'blogs': blogs, 'posts': posts, 'events': events}
    return render(request, 'base/home.html', x)


def user_input(request):
    error = ''
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        phone = request.POST['phone-number']
        email = request.POST['email']
        designation = request.POST['designation']
        file_object = request.FILES['profile-picture']
        try:
            Applicant.objects.create(first_name=first_name, last_name=last_name,
                                     phone=phone, email=email, designation=designation, profile_picture=file_object)
            error = 'no'
        except Exception as e:
            print(e)
            error = 'yes'
    x = {'error': error}
    return render(request, 'base/userInputForm.html', x)


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')