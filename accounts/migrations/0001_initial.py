""" Django Migrations """
# pylint: disable=line-too-long disable=invalid-name

import uuid
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Migration """
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('pkid', models.BigAutoField(
                    editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255,
                 unique=True, verbose_name='Email Address')),
                ('role', models.CharField(choices=[
                 ('default', 'Default'), ('admin', 'Admin')], db_index=True, default='default', max_length=20)),
                ('first_name', models.CharField(
                    max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(
                    max_length=255, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
