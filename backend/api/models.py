from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin, Permission
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, name, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)  

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
