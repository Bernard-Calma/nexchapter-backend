# Generated by Django 4.1.7 on 2023-03-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_manga_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='current_chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manga',
            name='image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
