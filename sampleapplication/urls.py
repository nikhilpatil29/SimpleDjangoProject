from django.conf.urls import url
from .views import index, home_page, login_page, register_page, log_out

urlpatterns = [
    url(r'^$', index, name = "index"),
    url(r'^login/$', login_page, name = "login"),
    url(r'^logout/$', log_out, name = "logout"),
    url(r'^registration/$', register_page, name = "registration"),
    url(r'^home/$', home_page, name = "home"),
]