# Generated by Django 4.0.3 on 2022-04-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_applicant_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='response',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=9, null=True),
        ),
    ]
