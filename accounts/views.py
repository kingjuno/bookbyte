from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from books.models import Book
from django.contrib.auth import get_user_model
from request_book.models import Req

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')  
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def profile_view(request,name):
    userid = get_user_model()
    name=userid.objects.get(username=name)
    try:
        created = Book.objects.all().filter(user=name)
    except:
        created = []
    try:
        req = Req.objects.all().filter(user=name)
    except:
        req = []
    return render(request,'profile.html',{'created':created,'req':req})