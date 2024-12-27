from django.urls import path
from . import views
urlpatterns = [
    path('swagertest/', views.test_swagger, name='swagertest'),
]