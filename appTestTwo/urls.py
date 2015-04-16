from django.conf.urls import include, url
import appTestTwo.views

urlpatterns = {
    url(r'^hello_world', appTestTwo.views.hello_world)
}