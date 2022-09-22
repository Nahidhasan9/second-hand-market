# Generated by Django 3.0.4 on 2020-04-30 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PostAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('condition', models.CharField(blank=True, choices=[('NEW', 'New'), ('USED', 'Used')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PostCategory')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='post.LocationCategoryModel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]