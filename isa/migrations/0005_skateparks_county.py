# Generated by Django 4.2.6 on 2023-11-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0004_alter_skateparks_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='skateparks',
            name='county',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
