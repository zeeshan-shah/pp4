# Generated by Django 3.2.21 on 2023-09-21 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_auto_20230920_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dish',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.mealcategory'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='customer.Dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(editable=False, max_length=10),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Street',
        ),
        migrations.DeleteModel(
            name='Zipcode',
        ),
    ]