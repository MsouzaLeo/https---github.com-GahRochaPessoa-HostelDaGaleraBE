# Generated by Django 3.2.4 on 2021-06-23 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='tipo_funcionario_id',
            new_name='tipo_funcionario',
        ),
    ]
