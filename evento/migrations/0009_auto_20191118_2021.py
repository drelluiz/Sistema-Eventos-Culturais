# Generated by Django 2.2.7 on 2019-11-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0008_auto_20191118_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='picture',
        ),
        migrations.AddField(
            model_name='evento',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='evento/'),
        ),
    ]
