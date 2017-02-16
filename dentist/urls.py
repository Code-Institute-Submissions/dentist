"""dentist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from dentist_app import views
from django.conf.urls import url, include
from accounts import views as accounts_views
from services import views as service_views
from appointments import views as appointment_views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index'),
    url(r'^ourteam/$', views.get_ourteam, name='ourteam'),

    #Authentication URLs
    url(r'^membership/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),

    #Blog URLs
    url(r'^blog/', include('reusable_blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    #Services URLs
    url(r'^services/$', service_views.all_services, name='services'),

    #Appointments URLs
    url(r'^appointments/$', appointment_views.all_appointments, name='appointments'),


]
