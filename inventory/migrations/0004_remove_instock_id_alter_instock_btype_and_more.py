from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_delete_used'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='instock',
        #     name='id',
        # ),
        migrations.AlterField(
            model_name='instock',
            name='Btype',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Coll',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Comp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='instock',
            name='CompID',
            field=models.AutoField(primary_key=True),
        ),
        migrations.AlterField(
            model_name='instock',
            name='Did',
            field=models.IntegerField(),
        ),
    ]
