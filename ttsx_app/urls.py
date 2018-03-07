from django.conf.urls import url,include
from ttsx_app import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^head/$', views.base),
    # url(r'^login/', views.logins, name='user_login'),
]