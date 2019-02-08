from django.db import models

class Atracao(models.Model):
	nome = models.CharField('Nome', max_length=100)
	tipo = (

          ('A', 'Adulto'),
          ('I', 'Infantil'),
          ('R', 'Religioso'),
		)
	decricao = models.TextField('Descrição')
	categoria = models.CharField('Categoria', max_length=1, choices=tipo)
	foto = models.ImageField(upload_to='img_atracoes', null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Atrações'
		verbose_name = 'Atração'

	def __str__(self):
		return self.nome