# Generated by Django 3.2.9 on 2021-12-17 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0006_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='awardsapp.profile'),
        ),
    ]
