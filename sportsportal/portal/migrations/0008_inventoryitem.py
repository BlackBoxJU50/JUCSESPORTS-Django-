# Generated by Django 5.2.1 on 2025-06-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_galleryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('In Use', 'In Use'), ('Damaged', 'Damaged')], default='Available', max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
