from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('services/', views.service_view, name='services'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



