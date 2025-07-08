from django.urls import path #Importa pacotes de URLS
from . import views #Importa o arquivo views.py do mesmo app

urlpatterns = [
    path('login/', views.login_view, name='login') #Rota: /login/ vai chamar a função login_view
]
