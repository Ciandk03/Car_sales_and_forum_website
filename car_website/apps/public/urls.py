
from django.urls import path
from . import views

app_name = "public"
urlpatterns = [
    path('', views.index, name="index"),
    path('used', views.used, name="used"),
    path('contact', views.contact, name="contact")
]