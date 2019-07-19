"""vist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path
import count_app.views as count


app_name = 'count_app'

urlpatterns = [
    re_path(r'^$', count.CountListView.as_view(), name='count_list'),
    re_path(r'^login/$', count.CountLoginView.as_view(), name='login'),
    re_path(r'^logout/$', count.CountLogoutView.as_view(), name='logout'),
    re_path(r'^register/$', count.UserRegister.as_view(), name='register'),
    re_path(r'^update/(?P<pk>\d+)$', count.CounterUpdate.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)$', count.CounterDelete.as_view(), name='delete'),

]
