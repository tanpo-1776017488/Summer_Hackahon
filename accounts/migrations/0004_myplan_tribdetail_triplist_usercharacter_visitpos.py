# Generated by Django 3.1.3 on 2021-08-07 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='myplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15, null=True)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('is_finished', models.BooleanField(default=False)),
                ('hp', models.IntegerField(default=5)),
                ('eat', models.IntegerField(default=5)),
                ('budget', models.IntegerField(default=5)),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='여행 도시')),
                ('Transportation', models.CharField(blank=True, max_length=15, null=True)),
                ('memo', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tripList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=15)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('budget', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='VisitPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(blank=True, max_length=15, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.myplan')),
            ],
        ),
        migrations.CreateModel(
            name='UserCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=15)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tribDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='여행 이미지')),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.triplist')),
            ],
        ),
    ]