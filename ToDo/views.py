from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import TodoItemSerializer

@api_view(['POST'])
def create_item(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_items(request):
    queryset = ToDo.objects.all()
    serializer = TodoItemSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_item(request, pk):
    try:
        product = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TodoItemSerializer(product)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def update_item(request, pk):
    try:
        product = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TodoItemSerializer(product, data=request.data, initial= True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    item.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)