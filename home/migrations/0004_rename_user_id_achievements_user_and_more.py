# Generated by Django 4.1.5 on 2023-01-25 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_user_achievements_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievements',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='analytics',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='drink_id',
            new_name='drink',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userlists',
            old_name='user_id',
            new_name='user',
        ),
    ]