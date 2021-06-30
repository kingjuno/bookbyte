from django.shortcuts import render,redirect
from books.models import Book
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from . import forms
from exchange import forms as form2
from django.http import HttpResponseRedirect

def book_list(request):
    books = Book.objects.all().order_by('date')
    return render(request,'book_list.html',{'books': books})

def book_detail(request,user,slug):
    userid = get_user_model()
    user=userid.objects.get(username=user)
    book = Book.objects.get(url_id=slug,user=user)
    if request.method == 'POST':
        form = form2.CreateLoc(request.POST)
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
    return render(request,'book_detail.html',{'book': book,'form': form})

def book_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = forms.CreateArticle()
    return render(request,'book_create.html',{'form': form})