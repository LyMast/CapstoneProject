# Generated by Django 4.1.1 on 2022-11-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('usernum', models.SmallAutoField(db_column='UserNum', primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, db_column='ID', max_length=128, null=True, unique=True)),
                ('pass_field', models.CharField(blank=True, db_column='PASS', max_length=128, null=True)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=32, null=True)),
                ('userphonenum', models.CharField(blank=True, db_column='UserPhoneNUM', max_length=32, null=True, unique=True)),
                ('e_mail', models.CharField(blank=True, db_column='E_Mail', max_length=256, null=True, unique=True)),
                ('userage', models.IntegerField(blank=True, db_column='UserAge', null=True)),
                ('commonusertype', models.IntegerField(blank=True, db_column='CommonUserType', null=True)),
                ('adminusertype', models.IntegerField(blank=True, db_column='AdminUserType', null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('targetnum', models.SmallAutoField(db_column='TargetNum', primary_key=True, serialize=False)),
                ('targetname', models.CharField(blank=True, db_column='TargetName', max_length=32, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=1, null=True)),
                ('image', models.TextField(blank=True, db_column='Image', null=True)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('targetage', models.IntegerField(blank=True, db_column='TargetAge', null=True)),
                ('missingornot', models.IntegerField(blank=True, db_column='MissingOrNot', null=True)),
                ('urgentnum', models.CharField(blank=True, db_column='UrgentNum', max_length=32, null=True)),
                ('usernum', models.ForeignKey(db_column='UserNum', on_delete=django.db.models.deletion.DO_NOTHING, to='backend_appUser.user')),
            ],
            options={
                'verbose_name': 'Target',
                'verbose_name_plural': 'Target',
                'db_table': 'Target',
                'unique_together': {('targetnum', 'usernum')},
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('devicename', models.CharField(db_column='DeviceName', max_length=64, primary_key=True, serialize=False)),
                ('targetnum', models.ForeignKey(db_column='TargetNum', on_delete=django.db.models.deletion.DO_NOTHING, to='backend_appUser.target')),
                ('usernum', models.ForeignKey(db_column='UserNum', on_delete=django.db.models.deletion.DO_NOTHING, to='backend_appUser.user')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Device',
                'db_table': 'Device',
                'unique_together': {('devicename', 'targetnum', 'usernum')},
            },
        ),
    ]
