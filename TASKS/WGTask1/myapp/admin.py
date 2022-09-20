
from django.contrib import admin
from .models import User, Movies, Cinema, Screen, Movie_Run, Actor, Movie_Cast

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username','password','email','role']

@admin.register(Movies)
class AdminMovie_s(admin.ModelAdmin):
    list_display= ['movie', 'release_date','durations']

@admin.register(Cinema)
class AdminCinema(admin.ModelAdmin):
    list_display= ['cinema_name', 'address', 'number_of_screen']

@admin.register(Screen)
class AdminScreen(admin.ModelAdmin):
    list_display= ['screen', 'cinema']

@admin.register(Movie_Run)
class AdminMovie_Run(admin.ModelAdmin):
    list_display= ['start_time', 'end_time', 'screen', 'movies']

@admin.register(Actor)
class AdminActor(admin.ModelAdmin):
    list_display= ['actor_name']

@admin.register(Movie_Cast)
class AdminMovie_Cast(admin.ModelAdmin):
    list_display= ['character_name', 'movies', 'actor']



