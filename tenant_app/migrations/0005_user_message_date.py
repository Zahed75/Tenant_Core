# Generated by Django 3.2.9 on 2022-04-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_app', '0004_user_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_message',
            name='date',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
