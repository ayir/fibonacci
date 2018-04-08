from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.fib_number, name='fib_number')
]