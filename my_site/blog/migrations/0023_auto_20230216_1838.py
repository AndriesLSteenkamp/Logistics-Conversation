# Generated by Django 3.2.8 on 2023-02-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]