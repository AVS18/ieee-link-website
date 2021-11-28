# Generated by Django 3.2.9 on 2021-11-26 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DropNav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SideDropNav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=50)),
                ('side_nav', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.dropnav')),
            ],
        ),
        migrations.AddField(
            model_name='dropnav',
            name='main_nav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.navbar'),
        ),
    ]
