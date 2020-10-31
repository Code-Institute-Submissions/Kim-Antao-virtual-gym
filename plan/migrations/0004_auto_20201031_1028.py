# Generated by Django 3.1.2 on 2020-10-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20201031_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberregistration',
            name='bmi',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriberregistration',
            name='customer_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriberregistration',
            name='goal',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriberregistration',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
