# Generated by Django 4.2.2 on 2023-09-01 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=10, verbose_name='Id do trabalho')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Trabalho',
                'verbose_name_plural': 'Trabalhos',
                'ordering': ('titulo', 'identificador'),
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('A', 'Avaliado')], default='P', max_length=1, verbose_name='Status')),
                ('avaliador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Avaliador')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modulo.trabalho', verbose_name='Trabalho')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'ordering': ('trabalho', 'avaliador'),
            },
        ),
    ]