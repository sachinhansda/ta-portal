# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-18 19:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('department', models.CharField(default='', max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Admin')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='assistant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='assisting',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher_preference',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher_preference',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Course'),
        ),
        migrations.AlterField(
            model_name='assistant_preference',
            name='assistant',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='assisting',
            name='assistant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='teacher_preference',
            name='assistant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Assistant',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='teaching',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course'),
        ),
        migrations.AddField(
            model_name='teaching',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]