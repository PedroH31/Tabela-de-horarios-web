# Generated by Django 5.1.2 on 2025-03-15 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('semestre_vigencia', models.CharField(max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComponenteCurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('abreviatura', models.CharField(blank=True, max_length=50, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('periodo_diurno', models.BooleanField(default=False)),
                ('periodo_noturno', models.BooleanField(default=False)),
                ('ch_teorica', models.IntegerField(default=0)),
                ('ch_pratica', models.IntegerField(default=0)),
                ('grade_curricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gradecurricular')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('semestre', models.CharField(max_length=10)),
                ('grade_curricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gradecurricular')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('tipo', models.IntegerField(choices=[(1, 'Turmas Fixas'), (2, 'Vagas Fixas')])),
                ('parametros', models.JSONField(default=dict)),
                ('alocacao', models.JSONField(default=dict)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.horario')),
            ],
        ),
    ]
