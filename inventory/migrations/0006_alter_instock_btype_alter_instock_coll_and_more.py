# Generated by Django 5.1.1 on 2024-10-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_instock_compid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instock',
            name='Btype',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Coll',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Comp',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='instock',
            name='CompID',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Did',
            field=models.CharField(max_length=20),
        ),
    ]
