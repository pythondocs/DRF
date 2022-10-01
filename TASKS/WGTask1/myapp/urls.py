from django.urls import path
from myapp.views import UserRegistrationView, UserLoginView, MovieView, ActorView, UserProfileView, UserProfileViewG

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('movie/', MovieView.as_view(), name='movie'),
    path('actor/', ActorView.as_view(), name='actor'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile1/', UserProfileViewG.as_view(), name='profile'),

]