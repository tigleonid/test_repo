# Generated by Django 4.0.3 on 2022-06-07 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_markdownpage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepage',
            name='main_lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages_as_lect', to='main.lectureruser'),
        ),
    ]
