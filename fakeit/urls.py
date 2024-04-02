from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Ruta para la URL raíz
    path('fakeit/', include('fakeit.urls')),  # Ruta para las vistas de tu aplicación
]