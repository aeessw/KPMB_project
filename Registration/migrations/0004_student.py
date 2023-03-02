# Generated by Django 4.0.5 on 2022-12-27 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_course_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.course')),
            ],
        ),
    ]
