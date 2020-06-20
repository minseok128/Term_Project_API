from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Extinguisher
from .serializers import ExtinguisherSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world")


@api_view(['GET'])
def Show_extinguisher(request):
    totalExtinguisher = list(Extinguisher.objects.all())
    serializer = ExtinguisherSerializer(totalExtinguisher, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Show_extinguisher_num(request, id):
    ExtinguisherByNum = Extinguisher.objects.get(num=id)
    serializer = ExtinguisherSerializer(ExtinguisherByNum)
    return Response(serializer.data)
