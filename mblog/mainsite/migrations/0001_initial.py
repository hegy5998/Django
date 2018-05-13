# Generated by Django 2.0.5 on 2018-05-12 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(blank=True, max_length=20, null=True)),
                ('product_num', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('cateid', models.AutoField(primary_key=True, serialize=False)),
                ('catename', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('proname', models.CharField(blank=True, max_length=20, null=True)),
                ('proprice', models.IntegerField(blank=True, null=True)),
                ('procont', models.CharField(blank=True, max_length=255, null=True)),
                ('pronum', models.IntegerField(blank=True, null=True)),
                ('proimg', models.CharField(blank=True, max_length=255, null=True)),
                ('proid', models.CharField(blank=True, max_length=45, primary_key=True, serialize=False)),
                ('procate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Cate')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('adress', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Shop'),
        ),
    ]
