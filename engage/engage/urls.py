"""engage URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings


from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/post/(?P<pk>\d+)', views.blog_detail, name='blog_detail'),
    url(r'^housing/$', views.housing, name='housing'),  
    url(r'^food/$', views.food, name='food'),
    url(r'^transportation/$', views.transportation, name='transportation'),
    url(r'^entertainment/$', views.entertainment, name='entertainment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



