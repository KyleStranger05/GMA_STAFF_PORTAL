# Generated by Django 3.2 on 2021-09-15 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210915_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Include_opening_balances',
            new_name='tbytd_Include_opening_balances',
        ),
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Only_use_main_accounts',
            new_name='tbytd_Only_use_main_accounts',
        ),
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Print_account',
            new_name='tbytd_Print_account',
        ),
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Print_description',
            new_name='tbytd_Print_description',
        ),
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Print_null_values',
            new_name='tbytd_Print_null_values',
        ),
        migrations.RenameField(
            model_name='settingsclass',
            old_name='_tbytd_Sort_by_account_name',
            new_name='tbytd_Sort_by_account_name',
        ),
    ]
