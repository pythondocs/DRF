
from django.contrib import admin
from myapp.models import User, Movie, Cinema, Screen, MovieRun, Actor, MovieCast
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'name', 'email', 'role', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credential', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ( 'name', 'email', 'role',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'role', 'password1'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('id', 'username')
    filter_horizontal = ()
admin.site.register(User, UserModelAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','movie', 'release_date', 'durations', 'created_at', 'updated_at')
admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','actor_name', 'created_at', 'updated_at')
admin.site.register(Actor, ActorAdmin)

admin.site.register(Cinema)
admin.site.register(Screen)
admin.site.register(MovieRun)
admin.site.register(MovieCast)
