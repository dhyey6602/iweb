# Generated by Django 2.2.4 on 2019-10-05 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0004_hospital_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to=settings.AUTH_USER_MODEL),
        ),
    ]
