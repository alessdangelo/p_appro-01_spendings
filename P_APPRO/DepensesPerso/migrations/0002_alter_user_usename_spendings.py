# Generated by Django 4.1.6 on 2023-02-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepensesPerso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='useName',
            field=models.CharField(max_length=12),
        ),
        migrations.CreateModel(
            name='Spendings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speName', models.CharField(max_length=24)),
                ('speAmount', models.DecimalField(decimal_places=5, max_digits=5)),
                ('speDate', models.DateField()),
                ('speUsersInDebt', models.CharField(max_length=20)),
                ('speBoughtBy', models.ManyToManyField(to='DepensesPerso.user')),
            ],
        ),
    ]
