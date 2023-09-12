# Generated by Django 4.2.5 on 2023-09-12 05:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_pwd', models.CharField(max_length=255)),
                ('user_authority', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='post_images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=255)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]