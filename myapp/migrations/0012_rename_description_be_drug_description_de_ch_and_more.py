# Generated by Django 5.0.4 on 2024-06-22 08:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0011_drug_description_jp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drug",
            old_name="description_be",
            new_name="description_de_CH",
        ),
        migrations.RenameField(
            model_name="drug",
            old_name="description_ch",
            new_name="description_nl_BE",
        ),
        migrations.RenameField(
            model_name="drug",
            old_name="description_pr",
            new_name="description_pt",
        ),
    ]