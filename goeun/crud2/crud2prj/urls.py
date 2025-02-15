"""
URL configuration for crud2prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import crud2app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',crud2app.views.index02, name ='index02'),
    path('create/',crud2app.views.create, name = 'create'),
    path('read02/',crud2app.views.read02, name = 'read02'),
    path('detail02/<str:title>/',crud2app.views.detail02, name = 'detail02'),

    path('update02/<str:title>/',crud2app.views.update02, name = 'update02'),
    path('delete02/<str:title>/',crud2app.views.delete02, name ='delete02'),
]
