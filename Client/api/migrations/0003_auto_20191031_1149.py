# Generated by Django 2.2.6 on 2019-10-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191031_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
