# Generated by Django 2.1.5 on 2019-02-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default-user.png', upload_to='profile_pics'),
        ),
    ]