# Generated by Django 4.1.6 on 2023-02-17 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_login_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
