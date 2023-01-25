# Generated by Django 3.2.5 on 2023-01-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EusoMem',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=50)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('posi_cd', models.CharField(blank=True, max_length=10, null=True)),
                ('duty_resp_cd', models.CharField(blank=True, max_length=10, null=True)),
                ('dept_no', models.IntegerField(blank=True, db_column='dept_no', null=True)),
                ('zip_no', models.CharField(blank=True, max_length=50, null=True)),
                ('mem_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('join_dt', models.CharField(blank=True, max_length=8, null=True)),
                ('mem_stat_cd', models.CharField(blank=True, max_length=10, null=True)),
                ('reg_mem_no', models.IntegerField(blank=True, null=True)),
                ('modf_mem_no', models.IntegerField(blank=True, null=True)),
                ('reg_dt', models.DateTimeField()),
                ('modf_dt', models.DateTimeField(blank=True, null=True)),
                ('del_yn', models.CharField(blank=True, max_length=1, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'euso_mem',
                'ordering': ['-join_dt'],
                'managed': True,
            },
        ),
    ]
