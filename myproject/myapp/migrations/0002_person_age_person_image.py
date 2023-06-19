# Generated by Django 4.2 on 2023-04-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default='image', upload_to='media/'),
            preserve_default=False,
        ),
    ]