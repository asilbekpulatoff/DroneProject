from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from user.views import SignUpView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('admin/', admin.site.urls),
    path('directory/', include('directory.urls')),
    path('spravichnik/', include('spravchnik.urls')),
    path("auth/singup/", SignUpView.as_view(), name="signup"),
    path("auth/", include("django.contrib.auth.urls")),
]