# Generated by Django 4.1.7 on 2023-05-25 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0003_remove_historialeczenia_recepta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recepty',
            old_name='zalecane_leki',
            new_name='zalecone_leki',
        ),
        migrations.RemoveField(
            model_name='pensjonariusz',
            name='historia_leczenia',
        ),
        migrations.RemoveField(
            model_name='pensjonariusz',
            name='lekarze',
        ),
    ]
