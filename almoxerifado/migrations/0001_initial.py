# Generated by Django 3.2.15 on 2022-11-03 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Tipo de Material')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
            ],
            options={
                'verbose_name': 'Tipo de Material',
                'verbose_name_plural': 'Tipos de Materiais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome do Material')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxerifado.tipo_material')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxerifado.material')),
            ],
            options={
                'verbose_name': 'Estoque do Material',
                'verbose_name_plural': 'Estoque dos Materiais',
                'ordering': ['material__nome'],
            },
        ),
    ]
