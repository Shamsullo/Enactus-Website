# Generated by Django 3.0.5 on 2020-04-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutEnactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicAdvisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('position', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num1', models.CharField(max_length=30)),
                ('phone_num2', models.CharField(max_length=30)),
                ('phone_num3', models.CharField(max_length=30)),
                ('insta_link', models.CharField(max_length=150)),
                ('fb_link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('web_link', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]