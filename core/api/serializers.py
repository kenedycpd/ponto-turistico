from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
	comentarios = ComentarioSerializer(many=True)
	avaliacao = AvaliacaoSerializer(many=True)

	class Meta:
		model = PontoTuristico
		fields = ('id', 'nome', 'descricao', 'status', 'foto', 'comentarios', 'avaliacao')