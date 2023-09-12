import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("user_pwd", models.CharField(max_length=255)),
                ("user_name", models.CharField(max_length=10)),
                ("user_authority", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("post_title", models.CharField(max_length=255)),
                (
                    "post_content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("post_topic", models.CharField(max_length=10)),
                ("post_created_at", models.DateTimeField(auto_now_add=True)),
                ("post_views", models.IntegerField(default=0)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("comment_id", models.AutoField(primary_key=True, serialize=False)),
                ("comment_writer", models.CharField(max_length=255)),
                ("comment_content", models.TextField()),
                ("comment_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
        ),
    ]
