from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from request_book.models import Req

@login_required(login_url="/accounts/login")
def home(request):
    books = Book.objects.all().order_by('date')
    req = Req.objects.all().order_by('date')
    return render(request,'home.html',{'books': books,'request':req})