# Generated by Django 4.2.1 on 2023-06-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud2app', '0004_auto_20230626_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
