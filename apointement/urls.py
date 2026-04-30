from django.urls import path
from .views import add_apointement
urlpatterns = [
    path('' , add_apointement , name='add_apointement'),
]