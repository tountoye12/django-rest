
from rest_framework.response import Response

from rest_framework.decorators import api_view





def getData(request):
    person = {
        "name": "diallo",
        "age": 38
    }
    return Response(person)
