from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
CATEGORY_CHOICES = (
    ('Manager', 'Manager'),
    ('Viewer', 'Viewer'),
)
class UserManager(BaseUserManager):
    def create_user(self, username, email, name, role, password=None, password2=None):
        """
        Creates and saves a User with the given username, email, name, role and password.
        """
        if not username:
            raise ValueError('Users must have an Username')
        user = self.model(username=username, name=name, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, email, role, password=None):
        """
        Creates and saves a User with the given username, email, name, role and password.
        """
        user = self.create_user(username, name=name, email=email, role=role, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(verbose_name= 'username', max_length=100, unique=True)
    email = models.EmailField (max_length=255)
    name = models.CharField(max_length=100)
    role = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'role']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Movie(models.Model):
    movie = models.CharField(max_length=100)
    release_date = models.DateField()
    durations = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie

class Cinema(models.Model):
    cinema_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number_of_screen = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cinema_name

class Screen(models.Model):
    screen = models.CharField(max_length=100)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.screen

class MovieRun(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.actor_name

class MovieCast(models.Model):
    character_name = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE) 
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)