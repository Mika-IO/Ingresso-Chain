from django.urls import path
import core.views as core_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ingresschannel'
urlpatterns = [
    path('', core_views.home, name='home'),
    path('event', core_views.event, name='event'),
    path('dashboard', core_views.dashboard, name='dashboard')
    # path('buy/ticket')
    # path('advetiser')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)