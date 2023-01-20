from django.urls import path
from .views import IndexView,DetalheFuncionarioView

urlpatterns = [
    path('', IndexView.as_view(), name = 'IndexView'),
    path('detalhe/funcionario/<int:pk>/', DetalheFuncionarioView.as_view(), name = 'DetalheFuncionarioView'),
]