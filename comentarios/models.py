from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comentario = models.TextField('Comentarios')
	data = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField()

	verbose_name_plural = 'Comentarios'
	verbose_name = 'Comentario'

	def __str__(self):
		return self.user.username