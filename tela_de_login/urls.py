from django.contrib import admin
from django.urls import path, include #Adicione o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contas.urls')) #Conecta as rotas do app
]
