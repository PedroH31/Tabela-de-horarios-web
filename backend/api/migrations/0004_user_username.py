# Generated by Django 5.1.2 on 2025-03-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alocacao_pode_alterar_alocacao_pode_compartilhar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=255, unique=True),
        ),
    ]
