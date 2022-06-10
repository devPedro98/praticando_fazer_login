from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('login/', views.login_user, name='url_login_user'),
    path('login/submit', views.submit_login, name='url_submit_login'),
    # path('tela/', views.tela_login, name='url_tela_login'),
    path('teste/', views.ola, name='url_ola'),
    path('logout/', views.logout_user, name='url_logout'),

]
