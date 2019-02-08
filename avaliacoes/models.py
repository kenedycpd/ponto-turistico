from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comentario = models.TextField('Comentario')
	nota = models.DecimalField(max_digits=7, decimal_places=2)
	data = models.DateTimeField(auto_now_add=True)

	verbose_name_plural = 'Avaliações'
	verbose_name = 'Avaliação'

	def __str__(self):
		return self.user.username