# Generated by Django 2.2.2 on 2019-12-09 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_remove_profiles_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Eric Bello\\Documents\\Python\\ipnsite\\mediaprofiles'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='permission',
            field=models.SmallIntegerField(blank=True, default=1, null=True),
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('tittle', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=500)),
                ('type', models.SmallIntegerField()),
                ('addressed_to', models.SmallIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Eric Bello\\Documents\\Python\\ipnsite\\mediaimage')),
                ('file', models.FileField(blank=True, null=True, upload_to='C:\\Users\\Eric Bello\\Documents\\Python\\ipnsite\\mediadocuments')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Profiles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
