from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('dashbaord/', include('dashboard.urls')),
    path('accounts/', include('dashboard.urls')),
]
