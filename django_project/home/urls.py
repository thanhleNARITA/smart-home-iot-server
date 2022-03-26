from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('bloghome/', views.home, name='blog-home'),
    path('room/', views.smartHome, name='room'),

    path('', views.home, name='homepages'),
    path('security/', views.security, name='security'),
    path('aboutus/', views.aboutus, name='aboutus'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

serverURL = None
