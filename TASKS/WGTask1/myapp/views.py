from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from myapp.models import User, Movie, Actor
from myapp.serializers import UserRegistrationSerializer, UserLoginSerializer, MovieSerializer, UserProfileSerializer, ActorSerializer
from myapp.mypaginations import MyPageNumberPagination
from myapp.renderers import UserRenderer

# User Registration API
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Success'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Token funcation
def get_tokens_for_user(user):
    refresh= RefreshToken.for_user(user)

    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }

# User Login API
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
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

# Show User ProfileAPI
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

# RegisterAPI & ListAPI of Movie with Pagination & Search By Movie Name
class MovieView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['movie']

# RegisterAPI & ListAPI of Actor with Pagination & Search By Movie Name
class ActorView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['actor_name']

# # User Profile View API
# class UserProfileView(APIView):
#     renderer_classes = [UserRenderer]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, format=None):
#         serializer = UserProfileSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

