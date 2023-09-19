from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import accountsclass
from .serializers import accountserializer


@api_view(['POST'])
def post_accounts(request):
    data = {
        'Fname': request.data['Fname'],
        'Lname': request.data['Lname'],
        'booksname': request.data['booksname'],
        'age': request.data['age'],

    }

    ser = accountserializer(data=data)  # type: ignore
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_accounts(request):
    Accounts = accountsclass.objects.all()
    ser = accountserializer(Accounts, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_account(request, pk):
    try:
        Accounts = accountsclass.objects.get(pk=pk)
    except:
        return Response({"error": "not found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = accountserializer(Accounts)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ser = accountserializer(Accounts, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Accounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
