# Generated by Django 5.1.6 on 2025-02-17 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_contactmessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='Mensagens_de_Contactos',
        ),
    ]
