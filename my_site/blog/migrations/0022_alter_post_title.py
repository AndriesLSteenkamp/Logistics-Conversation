# Generated by Django 3.2.8 on 2023-02-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_profile_display_email_opt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=101),
        ),
    ]
