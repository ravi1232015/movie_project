# Generated by Django 3.0.2 on 2020-02-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bdate',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Theatre',
            new_name='Movie_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='noofseat',
            new_name='No_of_seat',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='mname',
            new_name='User_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pname',
        ),
    ]