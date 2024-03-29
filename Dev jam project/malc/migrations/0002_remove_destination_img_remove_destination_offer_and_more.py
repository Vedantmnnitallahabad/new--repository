# Generated by Django 4.1.6 on 2023-03-13 16:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('malc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='img',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('criticR', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
