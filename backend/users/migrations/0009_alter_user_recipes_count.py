# Generated by Django 4.2.13 on 2024-06-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_subscription_remove_user_recipes_user_recipes_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recipes_count',
            field=models.IntegerField(default=0),
        ),
    ]