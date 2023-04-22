# Generated by Django 4.0.6 on 2023-04-23 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_answer_theme_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='best_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_answer', to='api_app.answer'),
        ),
    ]