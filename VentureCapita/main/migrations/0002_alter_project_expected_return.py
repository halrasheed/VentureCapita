# Generated by Django 4.1.7 on 2023-02-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='expected_Return',
            field=models.CharField(choices=[('10%<##>30%', '10%<##>30%'), ('30%<##>50%', '30%<##>50%'), ('50%<##>70%', '50%<##>70%'), ('70%<##', '70%<##'), ('Other', 'Other')], max_length=200),
        ),
    ]
