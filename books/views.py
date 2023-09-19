from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import booksclass
from .serializers import bookserializers


@api_view(['POST'])
def post_books(request):
    data = {
        'name': request.data['name'],
        'genre': request.data['genre'],
        'Condition': request.data['Condition'],
    }

    ser = bookserializers(data=data)  # type: ignore
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
