from django.urls import path
import core.views as core_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ingressochain'
urlpatterns = [
    path('', core_views.home, name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)