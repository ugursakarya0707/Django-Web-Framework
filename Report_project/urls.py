from django.contrib import admin
from django.urls import path

from theblog.views import dashboard, frontpage, post_detail, profile

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('', profile, name='profile')
    ]
    
   