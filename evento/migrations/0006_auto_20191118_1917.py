# Generated by Django 2.2.7 on 2019-11-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0005_auto_20191118_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='banner',
            field=models.ImageField(blank=True, default=1, upload_to='evento/'),
            preserve_default=False,
        ),
    ]
