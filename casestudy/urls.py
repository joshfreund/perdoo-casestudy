from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='requests/')),
    path('requests/', include('newreq.urls')),
    path('accounts/', include('accounts.urls')),
    path('history/', include('logger.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

