
from rest_framework.response import Response

from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from product.models import Product







@api_view(['GET'])
def getData(request):
   products = Product.objects.all()
   serializer = ProductSerializer(products, many=True)

   return Response(serializer.data)


@api_view(['POST'])
def postProduct(request):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)
  else: 
     return Response({"msg": "Not valid data"})
   