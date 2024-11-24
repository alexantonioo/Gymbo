from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Reemplaza 'mi_aplicacion' con el nombre de tu aplicación
]


