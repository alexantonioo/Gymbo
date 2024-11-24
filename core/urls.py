from django.urls import path
from .views import login_view, client_dashboard, trainer_dashboard, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Agregar esta línea para manejar la raíz
    path('login/', login_view, name='login'),
    path('clients/dashboard/', client_dashboard, name='client_dashboard'),
    path('trainers/dashboard/', trainer_dashboard, name='trainer_dashboard'),
]





