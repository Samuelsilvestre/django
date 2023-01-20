from django.contrib import admin
from .models import Cargo, Servicos, Funcionario


@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
	pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass    	