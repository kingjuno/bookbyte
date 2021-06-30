from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include('books.urls')),
    path('view/',include('exchange.urls')),
    path('request/',include('request_book.urls')),
    path('accounts/',include('accounts.urls')),
    path('',views.home),
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)