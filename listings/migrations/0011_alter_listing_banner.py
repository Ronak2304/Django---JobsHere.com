# Generated by Django 5.0.4 on 2024-04-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_jobapplication_resume_alter_joblisting_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='banner',
            field=models.ImageField(null=True, upload_to='banner/images/'),
        ),
    ]
