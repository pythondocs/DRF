from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentUser
from .serializers import StudentSerializers
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            stu = StudentUser.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = StudentUser.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id=pk
        stu = StudentUser.objects.get(id=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            return Response(res, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id=pk
        stu = StudentUser.objects.get(id=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Partially Data Updated'}
            return Response(res, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id=pk
        stu=StudentUser.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted!!'})

        

