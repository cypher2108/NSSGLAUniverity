from django.shortcuts import render, redirect
from accounts.decorators import allowed_users, unauthenticated_user
from accounts.models import Account
from django.core.files.base import ContentFile
from django.core.mail import send_mail

from base.models import Applicant

# Create your views here.


@allowed_users(allowed_roles=['manager'])
def dashboard_home(request):
    return render(request, 'dashboard/dashboard-home.html')


@allowed_users(allowed_roles=['manager'])
def dashboard_application_request(request):
    if not request.user.is_authenticated:
        return redirect('login')
    application = Applicant.objects.all()
    context = {'application': application}
    return render(request, 'dashboard/dashboard-application-request.html', context)


@allowed_users(allowed_roles=['manager'])
def accept_application(request):
    error = ''
    if request.method == 'POST':
        application_id = request.POST['application-id']
        response = request.POST['response']
        application_id = int(application_id)
        try:
            application = Applicant.objects.filter(id=application_id)
            application.update(response=response, status=True)

            user = Account.objects.create_user(
                username=application[0].first_name + application[0].last_name,
                email=application[0].email,
                password=application[0].first_name
                + application[0].phone[-4:],
                first_name=application[0].first_name
            )
    
            user.last_name = application[0].last_name
            user.designation = application[0].designation
            user.mobile = application[0].phone
            profile_picture = ContentFile(application[0].profile_picture.read())
            new_picture_name = application[0].profile_picture.name.split("/")[-1]
            user.profile_picture.save(new_picture_name, profile_picture)
            user.save()

            send_mail(
                'Account Approved with NSSGLAU for' + application[0].first_name,
                'Hey, we have been approved your account with us(NSS GlA University) kinda.. test message',
                'nssglau@gmail.com',
                [user.email]
            )

            error = 'no'
        except Exception as e:
            print(e)
            error = 'yes'
    return redirect('dashboard-application-request')


@allowed_users(allowed_roles=['manager'])
def reject_application(request):
    error = ''
    if request.method == 'POST':
        application_id = request.POST['application-id']
        response = request.POST['response']
        application_id = int(application_id)
        try:
            application = Applicant.objects.filter(id=application_id)
            application.update(response=response, status=True)
            error = 'no'
        except:
            error = 'yes'
    return redirect('dashboard-application-request')
