# Generated by Django 2.2.6 on 2019-10-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('tipo', models.CharField(blank=True, choices=[('E', 'Estrutura'), ('I', 'Iluminação'), ('S', 'Som'), ('O', 'Outro')], max_length=1)),
                ('marca', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
                ('dimensao', models.CharField(blank=True, max_length=25, null=True)),
                ('valor', models.FloatField()),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
