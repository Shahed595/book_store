# Generated by Django 4.2.1 on 2023-06-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookstoreModel',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Sci-fi', 'Sci-fi'), ('Horror', 'Horor')], max_length=30)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateField()),
            ],
        ),
    ]