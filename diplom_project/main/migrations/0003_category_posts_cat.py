# Generated by Django 4.1.5 on 2023-02-19 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_posts_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category'),
        ),
    ]
