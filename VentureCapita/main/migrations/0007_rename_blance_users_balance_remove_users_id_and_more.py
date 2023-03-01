# Generated by Django 4.1.7 on 2023-03-01 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_users_blance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='blance',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AddField(
            model_name='project',
            name='sharesAvailable',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='sharesCount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='sharesValue',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]