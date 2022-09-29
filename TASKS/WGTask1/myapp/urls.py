from django.urls import path
from myapp.views import MovieListView, UserRegistrationView, UserLoginView, MovieView, UserProfileView, ActorView, ActorListView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('movie/', MovieView.as_view(), name='movie'),
    path('movielist/', MovieListView.as_view(), name='movielist'),
    path('actor/', ActorView.as_view(), name='actor'),
    path('actorlist/', ActorListView.as_view(), name='actorlist'),
]