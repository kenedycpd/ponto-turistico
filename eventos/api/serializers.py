from rest_framework.serializers import ModelSerializer
from eventos.models import Atracao

class AtracaoSerializer(ModelSerializer):
	class Meta:
		model = Atracao
		fields = '__all__'