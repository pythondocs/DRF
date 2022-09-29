from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Movie, Actor
from myapp.serializers import UserRegistrationSerializer, UserLoginSerializer, MovieSerializer, UserProfileSerializer, ActorSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from myapp.mypaginations import MyPageNumberPagination
from rest_framework.generics import ListAPIView

# Create your views here.
def get_tokens_for_user(user):
    refresh= RefreshToken.for_user(user)

    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Success'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username= serializer.data.get('username')
            password= serializer.data.get('password')
            user= authenticate(username=username, password=password)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK) 
            else:
                return Response({'errors':{'non_field_errors':['Username or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.data)
        return Response(serializer.data)

# RegisterAPI of Movie's
class MovieView(APIView):
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Movie Register!!'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ListAPI of Movie's
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MyPageNumberPagination

# RegisterAPI of Actor's
class ActorView(APIView):
    def post(self, request, format=None):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Actor Register!!'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)