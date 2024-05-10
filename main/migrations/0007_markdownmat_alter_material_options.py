# Generated by Django 4.0.3 on 2022-05-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_coursepage_lecturer_block_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkdownMat',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.material')),
                ('text', models.TextField()),
            ],
            bases=('main.material',),
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['id'], 'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
    ]
