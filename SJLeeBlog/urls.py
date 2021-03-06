"""SJLeeBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
admin.autodiscover()

"""urlpatterns = [
    url(r'^admin/', admin.site.urls),

]
"""

urlpatterns = patterns('',
	url(r'^$', 'MyBlog.views.index', name='home'),
    url(r'^add/$', 'MyBlog.views.add', name='add'),
    url(r'^add2/(\d+)/(\d+)/$', 'MyBlog.views.add2', name='add2'),
	url(r'^admin/', include(admin.site.urls)),
)