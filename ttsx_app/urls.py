from django.conf.urls import url,include
import views
urlpatterns = [
    # url(r'^$', views.index),
    # url(r'head', views.head),
    url(r'^login/', views.logins, name='user_login'),
]