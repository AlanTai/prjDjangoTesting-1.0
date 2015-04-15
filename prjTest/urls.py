from django.conf.urls import include, url
from django.contrib import admin
from appTest import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'prjTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # appTest
    url(r'^$', 'appTest.views.heelo_world', name='hello_world')
]
