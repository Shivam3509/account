from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager,AbstractUser
from django.contrib.auth.models import UserManager


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email),
            username=username
            
        )
        user.set_password(password)  # change password to hash
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email,username, is_admin=True, is_staff=True, is_active=True, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='Male')
    DOB = models.DateField(auto_now_add = True,null =True,blank = True)
    forgot_password_token = models.CharField(max_length=200,null=True,blank=True)
    expiry = models.BooleanField(default=False)
    email = models.EmailField(verbose_name='email address',max_length = 300, unique=True)
    username = models.CharField(max_length=200,unique=True,verbose_name='username')
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
