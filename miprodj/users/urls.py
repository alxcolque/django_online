from django.urls import path
from users import views as v

urlpatterns = [
    path('', v.inicio, name = 'inicio')
]