from django.conf.urls import url,include
from django.contrib import admin
from backend import views
urlpatterns = [
    url(r'^qwe/', views.qwe)
]