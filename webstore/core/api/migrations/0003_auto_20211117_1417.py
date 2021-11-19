# Generated by Django 3.2.9 on 2021-11-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211117_0941'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Type',
            new_name='UserType',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'cart', 'verbose_name_plural': 'carts'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'user type', 'verbose_name_plural': 'user types'},
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='api.Product', verbose_name='products'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='api.Product', verbose_name='products'),
        ),
        migrations.DeleteModel(
            name='ProductCart',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]