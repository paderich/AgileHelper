from django.contrib import admin
from django.urls import path
from core.views import index, about
from userprofile.views import signup
from django.contrib.auth.views import LoginView, LogoutView
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard')
]
