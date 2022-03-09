# Generated by Django 3.1.4 on 2021-01-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_image', models.ImageField(upload_to='', verbose_name="Tip's Image")),
                ('tip_english_text', models.TextField(verbose_name="Tip's English Text")),
                ('tip_arabic_text', models.TextField(verbose_name="Tip's Arabic Text")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Tip',
                'verbose_name_plural': 'Tips',
            },
        ),
    ]