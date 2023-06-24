from django.urls import path
from . import views

urlpatterns = [
    path('material/types', views.MaterialTypeListCreate.as_view()),
    path('material/types/<int:pk>', views.MaterialTypeRetrieveUpdateDestroy.as_view()),
    path('login/', views.login)
]
