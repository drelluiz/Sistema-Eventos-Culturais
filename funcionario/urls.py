from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'funcionario'

urlpatterns = [

    path('', views.funcionario_list, name='funcionario_list'), 
    path('cadastrar/', views.funcionario_create, name='funcionario_create'), 
    path('<int:pk>/', views.funcionario_detalhe, name='funcionario_detail'),
    #path('<int:pk>/editar/', views.FuncionarioUpdate.as_view(), name='funcionario_edit'),
    path('<int:pk>/deletar/', views.funcionario_delete, name='funcionario_delete'),
  
]
