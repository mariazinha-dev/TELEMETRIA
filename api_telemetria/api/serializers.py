from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador da marca do veículo'},
            'nome':{'help_text':'Nome da marca do veículo'}
        }

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador do modelo do veículo'},
            'nome':{'help_text':'Nome do modelo do veículo'}
        }

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador do veículo'},
            'descricao':{'help_text':'Tipo da medição realizada'},
            'marcaId':{'help_text':'Identificador da marca, buscar na api marca'},
            'modeloId':{'help_text':'Identificador do modelo, buscar na api modelo'},
            'ano':{'help_text':'Ano do veículo'},
            'horimetro':{'help_text':'Horas de funcionamento do veículo'}
        }

class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador da medição'},
            'tipo':{'help_text':'Tipo da medição realizada'},
            'unidadeMedidaId':{'help_text':'Identificador da unidade da medida, buscar na api unidade de medida'}
        }

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador da medição veículo'},
            'veiculoId':{'help_text':'Identificador do veículo, buscar na api veículo'},
            'medidaId':{'help_text':'Identificador da medida, buscar na api medida'},
            'data':{'help_text':'Data e hora da medição'},
            'valor':{'help_text':'Valor da mediçao'}
        }
        

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = "__all__"
        extra_kwargs={
            'id':{'help_text': 'Identificador da unidade de medida da medição'},
            'nome':{'help_text':'Nome da unidade de medida utilizada na medição'}
        }