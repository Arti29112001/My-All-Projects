# Generated by Django 4.1.3 on 2022-12-09 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminApp', '0003_rename_username_userinfo_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]