
from rest_framework.response import Response

from rest_framework.decorators import api_view

from .serializers import  ItemSerialier
from store.models import Item




@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerialier(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postItem(request):
    print(request.data)
    serializer = ItemSerialier(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)