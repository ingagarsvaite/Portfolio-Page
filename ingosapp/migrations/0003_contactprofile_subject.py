# Generated by Django 4.2.4 on 2023-09-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingosapp', '0002_blog_certificate_contactprofile_media_portfolio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactprofile',
            name='subject',
            field=models.TextField(default=0, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
