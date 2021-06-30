from django.shortcuts import render,redirect
from django.http import HttpResponse
from request_book.models import Req
from django.contrib.auth import get_user_model
from . import forms
from django.http import HttpResponseRedirect
from exchange import forms as form2

# Create your views here.
def request_create(request):
    if request.method == 'POST':
        form = forms.CreateReq(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = forms.CreateReq()
    return render(request,'request_create.html',{'form': form})

def request_detail(request,user,slug):
    userid = get_user_model()
    user=userid.objects.get(username=user)
    req = Req.objects.get(url_id=slug,user=user)
    if request.method == 'POST':
        form = form2.CreateLoc(request.POST)
        print(form.is_valid())
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            instance.client=user
            instance.bk=slug
            if(instance.user==instance.client):
                return render(request,'404.html')
            instance.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = form2.CreateLoc()
    return render(request,'request_detail.html',{'book': req,'form':form})