"""定义learning_logs的url模式"""
from django.conf.urls import url
from . import views
app_name = '[learning_log]'
urlpatterns = [
    #主页
    url('^$', views.index, name='index'),
]