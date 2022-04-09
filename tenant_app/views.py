from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from tenant_app.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    dict = {}
    return render(request, 'tenant_app/index.html', context=dict)


@login_required()
def user_dashboard(request):
    t_dashboard = TenantDashboard.objects.filter(user=request.user)
    print(t_dashboard)
    apt_info = ApartmentInfo.objects.filter(user=request.user)
    total_amount = 0
    total = 0
    # for item in apt_info:
    #     total_amount += item.total_amount

    u_message = User_Message.objects.filter(user=request.user)
    print(u_message)

    dict = {'t_dashboard': t_dashboard, 'apt_info': apt_info, ' u_message': u_message}

    return render(request, 'tenant_app/user.html', context=dict)


def Admin_dashboard(request):
    a_dashboard = admin_dashboard.objects.all()
    parking_fees = Parking_Fees.objects.all()
    print(parking_fees)
    dict = {'a_dashboard': a_dashboard, 'parking_fees': parking_fees}

    return render(request, 'tenant_app/admin.html', context=dict)
