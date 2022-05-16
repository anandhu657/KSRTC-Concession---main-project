# Generated by Django 3.2 on 2021-04-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_details_kcno'),
    ]

    operations = [
        migrations.CreateModel(
            name='app_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_dte', models.CharField(max_length=20)),
                ('student_id', models.IntegerField()),
                ('institution_id', models.IntegerField()),
                ('depot_id', models.IntegerField()),
                ('route_id', models.IntegerField()),
                ('src', models.CharField(max_length=50)),
                ('dest', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='bus_type_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='consession_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('stage_rate', models.FloatField()),
                ('dt', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('no_months', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='depot_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('dpname', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('adr1', models.CharField(max_length=300)),
                ('adr2', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=10)),
                ('ph', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('lno', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fdbck', models.CharField(max_length=1000)),
                ('dt', models.CharField(max_length=20)),
                ('tm', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='institution_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adrs1', models.CharField(max_length=200)),
                ('adrs2', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=20)),
                ('ph', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('affili', models.CharField(max_length=50)),
                ('govtpvt', models.CharField(max_length=20)),
                ('princi_name', models.CharField(max_length=50)),
                ('princi_ph', models.CharField(max_length=20)),
                ('i_type', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='rate_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_type_id', models.IntegerField()),
                ('stage', models.IntegerField()),
                ('fare', models.FloatField()),
                ('month_fare', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='route_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depot_id', models.IntegerField()),
                ('route_name', models.CharField(max_length=100)),
                ('bus_type_id', models.IntegerField()),
                ('src', models.CharField(max_length=100)),
                ('dest', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='route_stop_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('stop_id', models.IntegerField()),
                ('stop_no', models.IntegerField()),
                ('stop_stage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='stop_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depot_id', models.IntegerField()),
                ('stop_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('addr1', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('dist', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=50)),
                ('g_contact', models.CharField(max_length=20)),
                ('p_contact', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('institution_id', models.IntegerField()),
                ('dt', models.CharField(max_length=20)),
                ('tm', models.CharField(max_length=20)),
                ('pic', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]