# Generated by Django 4.1.4 on 2022-12-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Employee_id',
            field=models.CharField(max_length=10),
        ),
    ]