from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.http import request
from django.contrib import messages


from .models import Funcionario, Servicos, Cargo

#cçass da pagina index
class IndexView(TemplateView):
	template_name = 'IndexView.html'

	### metodo que exibe os contestos  
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['funcionarios'] = Funcionario.objects.all()
		context['servicos'] = Servicos.objects.all()
		return context


class DetalheFuncionarioView(DetailView):
	model = Funcionario
	template_name = 'DetalheFuncionarioView.html'

	
	
	

	


		

