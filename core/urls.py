from django.urls import path
import core.views as core_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ingresschannel'
urlpatterns = [
    path('', core_views.home, name='home'),
    path('policies', core_views.policies, name='policies'),
    # Buyer URLs
    path('event', core_views.event, name='event'),
    # Seller URLs
    path('dashboard', core_views.dashboard, name='dashboard'),
    path('create_event', core_views.create_event, name='create_event'),
    path('withdraw_historic', core_views.withdraw_historic, name='withdraw_historic'),
    path('report', core_views.report, name='report'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)