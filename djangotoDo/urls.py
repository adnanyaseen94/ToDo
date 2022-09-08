from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('', TemplateView.as_view(template_name='index.html')),
]
