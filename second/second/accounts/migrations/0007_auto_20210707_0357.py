# Generated by Django 3.2.3 on 2021-07-07 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_person_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='documents',
            field=models.FileField(default='default.jpg', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
