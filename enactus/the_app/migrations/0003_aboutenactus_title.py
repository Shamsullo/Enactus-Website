# Generated by Django 3.0.5 on 2020-04-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0002_aboutenactus_academicadvisors_contact_partners_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutenactus',
            name='title',
            field=models.CharField(default='non', max_length=100),
            preserve_default=False,
        ),
    ]