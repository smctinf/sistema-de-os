# Generated by Django 3.2.14 on 2022-11-17 17:46

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
                ('qnt_em_estoque', models.IntegerField(blank=True, default=0, null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.tipo_material')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
                'ordering': ['tipo__nome', 'nome', 'qnt_em_estoque'],
            },
        ),
        migrations.CreateModel(
            name='Log_estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_quantidade', models.IntegerField(verbose_name='Quantidade p/ adicionar ao estoque')),
                ('qnt_em_estoque', models.IntegerField(null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.material')),
            ],
            options={
                'verbose_name': 'Log do estoque do material',
                'verbose_name_plural': 'Log do estoque dos materiais',
                'ordering': ['material__nome'],
            },
        ),
    ]