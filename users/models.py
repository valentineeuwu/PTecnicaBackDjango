from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError('Users must have username value')
        else:
            parsed_email = ''
        user = self.model(
            username=username,
            email=parsed_email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    password = models.CharField(max_length=200)
    image = models.CharField(max_length=300)

    first_name = None
    last_name = None
    last_login = None

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
