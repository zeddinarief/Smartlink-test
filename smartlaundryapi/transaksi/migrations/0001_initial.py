# Generated by Django 3.1.1 on 2020-09-15 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('layanan', '0001_initial'),
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transaction', models.CharField(max_length=6, unique=True)),
                ('pelanggan', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('diskon_persen', models.IntegerField()),
                ('diskon_rupiah', models.IntegerField()),
                ('tagihan', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.users')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('layanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layanan.services')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaksi.transactions')),
            ],
            options={
                'db_table': 'transaction_detail',
            },
        ),
    ]
