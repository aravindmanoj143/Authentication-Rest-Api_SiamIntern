# Generated by Django 2.2.6 on 2019-10-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='Email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='Mobile',
            field=models.CharField(max_length=50),
        ),
    ]