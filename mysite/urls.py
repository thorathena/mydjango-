"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog import views
from blog.views import Home,List,Detail, MyPostList, Myarticles,Delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^post/', List.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/', Detail.as_view(), name='post_detail'),
    url(r'^list/', MyPostList.as_view(), name='articlelist'),
    url(r'^article/(?P<pk>[0-9]+)/', Myarticles.as_view(), name='article'),
    url(r'^delete/(?P<pk>[0-9]+)/', Delete.as_view(), name='delete'),



]
