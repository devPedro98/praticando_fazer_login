from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.CriarConta.as_view(), name='url_criaar_conta'),
]
