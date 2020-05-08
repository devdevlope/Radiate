# Generated by Django 3.0.5 on 2020-05-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('answer_text', models.CharField(max_length=500)),
                ('set_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14)])),
            ],
        ),
    ]