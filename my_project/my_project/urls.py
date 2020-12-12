"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('avengers/',views.avengers),
    path('avengers2/',views.avengers2),
    path('avengers3/',views.avengers3),
    path('avengers4/',views.avengers4),
    path('batman1/',views.batman1),
    path('batman2/',views.batman2),
    path('batman3/',views.batman3),
    path('joker/',views.joker),
    path('blackwidow/',views.blackwidow),
    path('morbius/',views.morbius),
    path('birdsofprey/',views.birdsofprey),
    path('wonderwoman/',views.wonderwoman),
    path('movies/',views.movies),
    path('spiderman/',views.spiderman),
    path('manofsteel/',views.manofsteel),
    path('book/',views.book),
    path('about/',views.about),
    path('contact/',views.contact),
     path('success/',views.success)
]
