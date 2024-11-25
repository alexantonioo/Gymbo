# Generated by Django 5.1.3 on 2024-11-25 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerprofile',
            name='clients',
            field=models.ManyToManyField(related_name='trainers', to='core.clientprofile'),
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='whatsapp_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clientprofile')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clientprofile')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainerprofile')),
            ],
        ),
    ]
