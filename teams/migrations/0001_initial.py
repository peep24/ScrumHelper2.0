# Generated by Django 2.2.15 on 2021-10-15 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teams.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.TextField(blank=True, null=True)),
                ('team_image', models.ImageField(blank=True, default=teams.models.get_default_profile_image, max_length=255, null=True, upload_to=teams.models.get_profile_image_filepath)),
                ('leader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'ordering': ['-team_id'],
            },
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Teams')),
            ],
            options={
                'verbose_name_plural': 'Team Members',
                'ordering': ['-team_id'],
            },
        ),
    ]
