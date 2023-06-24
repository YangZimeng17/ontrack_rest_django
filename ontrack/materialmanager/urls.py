from django.urls import path
from . import views

app_name = 'materialmanager'

urlpatterns = [
    path('import/material_type', views.import_material_type, name='import_material_type'),
]
