# Generated by Django 3.1.5 on 2021-01-07 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLenguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('learning_difficulty', models.CharField(choices=[('easy', 'Fácil'), ('medium', 'Médio'), ('hard', 'HARD')], max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'FEMININO')], max_length=20)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=5)),
                ('programming_lenguage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.programminglenguage')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]