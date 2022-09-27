"""texteditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from texteditorapp import views

admin.site.site_header = "Text Editor By Parth Shah"
admin.site.site_title = "Text Editor"
admin.site.index_title = "Text Editor"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login1,name='login1'),
    path('logoutView/',views.logoutView,name='logoutView'),
    path('register',views.register,name='register'),
    path('index/', views.index,name="index"),
    path('analyze', views.analyze,name="analyze"),
    path('Contact/', views.Contact,name="Contact"),
    path('About/', views.About,name="About"),
    path('MiniProject/', views.MiniProject,name="MiniProject"),
    path('Websites/', views.Websites,name="Websites"),
    path('Applications/', views.Applications,name="Applications"),

]
