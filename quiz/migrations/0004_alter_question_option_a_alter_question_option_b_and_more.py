# Generated by Django 5.1.4 on 2024-12-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_correct_option_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option_a',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_b',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_c',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_d',
            field=models.CharField(max_length=100),
        ),
    ]