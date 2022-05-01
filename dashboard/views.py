from django.shortcuts import render, redirect
from accounts.decorators import allowed_users, unauthenticated_user

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

            error = 'no'
        except:
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
