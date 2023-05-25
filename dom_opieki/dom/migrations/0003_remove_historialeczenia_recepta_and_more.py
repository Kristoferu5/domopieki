# Generated by Django 4.1.7 on 2023-05-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0002_remove_pielegniarz_pracownik_remove_lekarz_pracownik_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialeczenia',
            name='recepta',
        ),
        migrations.AddField(
            model_name='historialeczenia',
            name='recepty',
            field=models.ManyToManyField(blank=True, related_name='historie_leczenia', to='dom.recepty'),
        ),
    ]
