from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api import serializers
from drf_yasg.utils import swagger_auto_schema

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.Marca.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de marcas",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de marca",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de marca conforme dados pessoais, para o ID informado",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de marca conforme ID informado",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ModeloSerializer
    queryset = models.Modelo.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de modelos",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de modelo",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de modelo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de modelo conforme dados pessoais, para o ID informado",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de modelo conforme ID informado",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoSerializer
    queryset = models.Medicao.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de medição",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição conforme ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme dados pessoais, para o ID informado",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de tipo de medição conforme ID informado",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
     
class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoVeiculoSerializer
    queryset = models.MedicaoVeiculo.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de medições dos veículos",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de medição do veículo",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de medição do veículo conforme ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de medição do veículo conforme dados pessoais, para o ID informado",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de medição do veículo conforme ID informado",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VeiculoSerializer
    queryset = models.Veiculo.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de veículos",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de veículo",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de veículo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de veículo conforme dados pessoais, para o ID informado",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de veículo conforme ID informado",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UnidadeMedidaSerializer
    queryset = models.UnidadeMedida.objects.all()

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de unidades de medidas",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de unidade de medida",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o registro de unidade de medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o tipo de unidade de medida conforme dados pessoais, para o ID informado",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de unidade de medida conforme ID informado",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
