# Generated by Django 2.0.2 on 2018-02-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LookupRajon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rajons', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lookup_rajon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LookupRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regions', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lookup_region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='First_name', max_length=100)),
                ('last_name', models.CharField(db_column='Last_name', max_length=100)),
                ('patron_name', models.CharField(db_column='Patron_Name', max_length=150)),
                ('date_birthday', models.DateField(blank=True, null=True)),
                ('phone_home', models.CharField(max_length=10)),
                ('phone_mobile', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=250)),
                ('place_of_work', models.TextField()),
                ('date_medical_examination', models.DateField(blank=True, null=True)),
                ('purpose_medical_examination', models.CharField(max_length=20)),
                ('reference_number', models.CharField(max_length=30)),
                ('validaty_days', models.IntegerField()),
                ('addr_locality', models.CharField(max_length=3)),
                ('addr_city', models.CharField(max_length=100)),
                ('addr_abbreavation', models.CharField(max_length=10)),
                ('addr_street', models.CharField(max_length=200)),
                ('addr_house', models.CharField(max_length=5)),
                ('addr_corpus', models.CharField(max_length=5)),
                ('addr_room', models.CharField(max_length=5)),
                ('addr_index', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'Patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
    ]
