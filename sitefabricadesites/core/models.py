from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
	data = models.DateTimeField(auto_now = True)

	#########
	class Meta:
		abstract = True

#class serviços
class Servicos(Base):
	descricao = models.TextField()

# class de cargos
class Cargo(models.Model):
    cargo = models.CharField(max_length = 100)

    def __str__(self):
        return self.cargo

    ######
    class Meta:
        db_table = 'Cargo'
        verbose_name_plural = 'Cargos'

class Funcionario(Base):
    nome = models.CharField(max_length = 100)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE)
    biografia = models.TextField()
    img = StdImageField('FOTO', upload_to = 'equipe', variations={'thumbnail' :  {'width': 600, 'height': 600, 'crop' : True}})
    facebook = models.URLField(blank = True, null = True)
    twitter = models.URLField(blank = True, null = True)
    instagram = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.nome        		

    ########
    class Meta:
    	db_table = 'Funcionario'
    	verbose_name_plural = 'Funcionarios'