from django.conf.urls import include, url
import appTestTwo.views

urlpatterns = [
    url(r'^$', appTestTwo.views.hello_world)
]