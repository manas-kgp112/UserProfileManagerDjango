# Generated by Django 4.0.4 on 2022-06-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_authuser_email_authuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]