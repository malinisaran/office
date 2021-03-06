# Generated by Django 4.0.1 on 2022-02-16 05:05

from django.db import migrations, models
import django.db.models.deletion
import stream.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.CharField(max_length=1024, verbose_name='playlist_name')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='video_name')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='stream.data')),
            ],
        ),
        migrations.CreateModel(
            name='ClientFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1024, storage=stream.models.MyFileSystemStorage, upload_to=stream.models.upload_path_handler)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_files', to='stream.data',db_constraint=False)),
            ],
            options={
                'unique_together': {('data', 'file')},
            },
        ),
    ]
