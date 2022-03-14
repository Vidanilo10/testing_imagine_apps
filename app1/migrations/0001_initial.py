# Generated by Django 4.0.3 on 2022-03-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer_field', models.IntegerField()),
                ('char_field', models.CharField(max_length=100)),
                ('value_type', models.CharField(choices=[('string', 'string'), ('int', 'int'), ('date', 'date'), ('money', 'money')], max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
    ]