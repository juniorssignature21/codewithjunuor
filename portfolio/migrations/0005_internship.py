# Generated by Django 5.0.6 on 2024-07-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('usn', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('college_name', models.CharField(max_length=100)),
                ('offer_status', models.CharField(max_length=60)),
                ('start_date', models.CharField(max_length=60)),
                ('end_date', models.CharField(max_length=60)),
                ('proj_report', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
