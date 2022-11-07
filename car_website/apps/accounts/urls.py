from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from ..accounts.views import forums

app_name = "accounts"
urlpatterns = [

    path('profile', views.Profileview.as_view(), name="profile"),
    # Django Auth
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('register', views.register, name="register"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('forums', forums.as_view(), name="forums")
]
