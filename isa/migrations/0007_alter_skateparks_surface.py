# Generated by Django 4.2.6 on 2023-11-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0006_alter_skateparks_helmets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skateparks',
            name='surface',
            field=models.CharField(choices=[('Concrete', 'Concrete'), ('Wood', 'Wood'), ('Unknown', 'Unknown')], max_length=20),
        ),
    ]
