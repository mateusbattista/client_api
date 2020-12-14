from rest_framework import serializers

from .models import Cliente

class ClientSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nome','email','telefone','endereco','servico_interessado')