# Generated by Django 4.0 on 2022-01-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='text',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='phone',
        ),
        migrations.AddField(
            model_name='sms',
            name='file',
            field=models.FileField(default='', upload_to='Data/'),
            preserve_default=False,
        ),
    ]
