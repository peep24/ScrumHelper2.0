# Generated by Django 2.2.15 on 2021-10-13 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_tasks_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('With client', 'With Client'), ('blocked', 'BLOCKED'), ('complete', 'COMPLETE')], default='active', max_length=40),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_id',
            field=models.CharField(max_length=14, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.CreateModel(
            name='AccountTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Tasks')),
            ],
            options={
                'verbose_name_plural': 'AccountTasks',
                'ordering': ['-task_id'],
            },
        ),
    ]