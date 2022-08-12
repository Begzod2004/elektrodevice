
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
# New
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('zero/', admin.site.urls),
    path('',include('website.urls')),
    # New!!!!!
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),  
]
