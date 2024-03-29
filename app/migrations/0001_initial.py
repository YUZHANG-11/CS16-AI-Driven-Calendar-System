# Generated by Django 5.0.3 on 2024-03-22 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=100)),
                ('deptorder', models.IntegerField(verbose_name=10)),
                ('status', models.SmallIntegerField(choices=[(1, 'normal'), (2, 'Deactivate')])),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=100)),
                ('order_num', models.IntegerField(verbose_name=10)),
                ('path', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(choices=[(1, 'normal'), (2, 'Deactivate')])),
                ('component', models.CharField(max_length=100)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'Catalogue'), (2, 'Menu'), (3, 'Button')])),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
                ('data_scope', models.SmallIntegerField(choices=[(1, 'All'), (2, 'NowDept'), (3, 'Basic')])),
                ('status', models.SmallIntegerField(choices=[(1, 'normal'), (2, 'Deactivate')])),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=11)),
                ('usertype', models.SmallIntegerField(choices=[(1, 'system_user'), (2, 'ordinary_user')])),
                ('email', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')])),
                ('create_time', models.DateField()),
                ('employment_time', models.DateField()),
                ('accoun_status', models.SmallIntegerField(choices=[(1, 'normal'), (2, 'Deactivate')])),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.role')),
            ],
        ),
    ]