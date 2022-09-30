from django.urls import path
from myapp.views import UserRegistrationView, UserLoginView, MovieView, UserProfileView, ActorView, UserRegistrationGenericView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('registerapi/', UserRegistrationGenericView.as_view(), name='registerapi'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('movie/', MovieView.as_view(), name='movie'),
    path('actor/', ActorView.as_view(), name='actor'),
]