# Generated by Django 5.0.3 on 2024-04-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('moodle', models.CharField(max_length=122)),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Phone',
            field=models.CharField(max_length=12),
        ),
    ]
