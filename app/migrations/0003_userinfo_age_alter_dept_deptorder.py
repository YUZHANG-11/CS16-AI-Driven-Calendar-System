# Generated by Django 5.0.3 on 2024-03-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_menu_order_num_remove_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dept',
            name='deptorder',
            field=models.IntegerField(verbose_name='order'),
        ),
    ]