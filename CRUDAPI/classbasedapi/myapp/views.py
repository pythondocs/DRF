from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu= StudentModel.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id=pk
        if id is not None:
            stu= StudentModel.objects.get(id=id)
            serializer= StudentSerializers(stu, data=request.data)
            return Response({'msg':'Complete Data Updated!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        id=pk
        if id is not None:
            stu= StudentModel.objects.get(id=id)
            serializer= StudentSerializers(stu, data=request.data, partial=True)
            return Response({'msg':'Partial Data Updated!!'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        stu = StudentModel.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted!!'}, status=status.HTTP_200_OK)
        