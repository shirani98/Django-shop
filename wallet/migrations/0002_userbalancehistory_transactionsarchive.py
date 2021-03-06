# Generated by Django 4.0 on 2022-03-24 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_username'),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='balance_history', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (3, 'Transfer')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_transaction_archive', to='accounts.user')),
            ],
        ),
    ]
