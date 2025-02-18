# Generated by Django 4.2.4 on 2023-08-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField()),
                ('category', models.CharField(default='none', max_length=10)),
            ],
        ),
    ]
