# Generated by Django 3.0.7 on 2020-07-02 16:48

from django.db import migrations, models
import django.db.models.deletion
import todolist.models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20200608_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='contry',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=todolist.models.image_upload),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('Website', models.URLField()),
                ('Upload_CV', models.FileField(upload_to='apply/')),
                ('Coverletter', models.TextField(max_length=60)),
                ('pub_dat', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='todolist.Post')),
            ],
        ),
    ]
