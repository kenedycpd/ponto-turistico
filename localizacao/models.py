from django.db import models


class Endereco(models.Model):
	linha1 = models.CharField('Rua', max_length=100)
	linha2 = models.CharField('Outros', max_length=100, null=True,blank=True)
	cidade = models.CharField('Cidade', max_length=50)
	estado = models.CharField('Estado', max_length=50)
	pais = models.CharField('Pais', max_length=50)

	verbose_name_plural = 'Endereço'

	def __str__(self):
		return self.linha1