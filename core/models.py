from django.db import models
from eventos.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Endereco

class PontoTuristico(models.Model):
	nome = models.CharField('Nome', max_length=100,)
	descricao = models.TextField('Descrição')
	status = models.BooleanField()
	atracao = models.ManyToManyField(Atracao)
	comentarios = models.ManyToManyField(Comentario)
	avaliacao = models.ManyToManyField(Avaliacao)
	localizacao = models.ForeignKey(Endereco, on_delete=models.CASCADE,null=True,blank=True)
	foto = models.ImageField(upload_to='img', null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Ponto Turisticos'
		verbose_name = 'Ponto Turistico'
		
	def __str__(self):
		return self.nome