# Generated by Django 3.1.3 on 2021-08-08 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_profile_p_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='triplist',
            name='content',
            field=models.TextField(blank=True, default='abc', null=True),
        ),
        migrations.AddField(
            model_name='triplist',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='triplist',
            name='budget',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
