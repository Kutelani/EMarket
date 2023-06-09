# Generated by Django 3.0.8 on 2020-08-20 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200818_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ZAR Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=200, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=30)),
                ('billingAddress1', models.CharField(blank=True, max_length=30)),
                ('billingCity', models.CharField(blank=True, max_length=30)),
                ('billingPostalCode', models.CharField(blank=True, max_length=30)),
                ('billingCountry', models.CharField(blank=True, max_length=30)),
                ('shippingName', models.CharField(blank=True, max_length=30)),
                ('shippingAddress1', models.CharField(blank=True, max_length=30)),
                ('shippingCity', models.CharField(blank=True, max_length=30)),
                ('shippingPostalCode', models.CharField(blank=True, max_length=30)),
                ('shippingCountry', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ZAR price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
