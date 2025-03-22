from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin, Permission
from django.contrib.auth import get_user_model
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


class GradeCurricular(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    semestre_vigencia = models.CharField(max_length=10) 
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pode_alterar = models.ManyToManyField(User, related_name="can_edit_grade_curricular", blank=True)
    pode_compartilhar = models.ManyToManyField(User, related_name="can_share_grade_curricular", blank=True)

    def __str__(self):
        return f"{self.nome} ({self.semestre_vigencia})"

# registro dentro da grade
class ComponenteCurricular(models.Model):
    grade_curricular = models.ForeignKey(GradeCurricular, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=255)
    abreviatura = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    periodo_diurno = models.BooleanField(default=False)
    periodo_noturno = models.BooleanField(default=False)
    ch_teorica = models.IntegerField(default=0) 
    ch_pratica = models.IntegerField(default=0)  

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Horario(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    semestre = models.CharField(max_length=10)  
    grade_curricular = models.ForeignKey(GradeCurricular, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pode_alterar = models.ManyToManyField(User, related_name="can_edit_horario", blank=True)
    pode_compartilhar = models.ManyToManyField(User, related_name="can_share_horario", blank=True)

    def __str__(self):
        return f"{self.nome} ({self.semestre})"


class Alocacao(models.Model):
    TIPO_CHOICES = [
        (1, "Turmas Fixas"),
        (2, "Vagas Fixas"),
    ]

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    parametros = models.JSONField(default=dict)  
    alocacao = models.JSONField(default=dict)
    pode_alterar = models.ManyToManyField(User, related_name="can_edit_alocacao", blank=True)
    pode_compartilhar = models.ManyToManyField(User, related_name="can_share_alocacao", blank=True)

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"
