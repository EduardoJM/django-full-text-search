# Generated by Django 4.2 on 2023-04-10 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('texto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texto.music', verbose_name='Musica')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texto.singer', verbose_name='Cantor')),
            ],
            options={
                'verbose_name': 'Participação Música',
                'verbose_name_plural': 'Participações Músicas',
            },
        ),
    ]
