from django.urls import path
from kafka_app import views

urlpatterns = [
    path('', views.SYNCapi.as_view())
]
