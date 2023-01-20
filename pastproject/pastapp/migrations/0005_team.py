# Generated by Django 3.2.16 on 2022-10-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastapp', '0004_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tesa')),
                ('names', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
    ]