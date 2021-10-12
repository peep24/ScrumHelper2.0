# Generated by Django 2.2.15 on 2021-10-12 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
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
