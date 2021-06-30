from django.shortcuts import render,redirect
from exchange.models import Location
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def notification(request):
    noti = Location.objects.all().filter(user=request.user)
    return render(request,'notification.html',{'noti': noti})