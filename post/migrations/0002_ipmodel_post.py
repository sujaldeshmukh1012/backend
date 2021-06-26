# Generated by Django 3.2.4 on 2021-06-26 10:40

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('picture', models.ImageField(upload_to='images', verbose_name='Picture')),
                ('title', models.TextField(max_length=500, null=True, verbose_name='Title')),
                ('id', autoslug.fields.AutoSlugField(editable=False, populate_from='title', primary_key=True, serialize=False)),
                ('body', djrichtextfield.models.RichTextField(default='', verbose_name='Body')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('tags', models.TextField(blank=True, default='blog')),
                ('categories', models.TextField(blank=True, default='blog')),
                ('likes', models.IntegerField(default=0)),
                ('isvisible', models.BooleanField(default=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('views', models.ManyToManyField(blank=True, to='post.IpModel')),
            ],
        ),
    ]
