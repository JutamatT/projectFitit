# Generated by Django 2.1.3 on 2019-08-26 19:11

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
            name='Profile',
            fields=[
                ('idShop', models.AutoField(primary_key=True, serialize=False)),
                ('nameShop', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dateTimeOpen', models.TimeField(blank=True, null=True)),
                ('dateTimeClose', models.TimeField(blank=True, null=True)),
                ('phone1', models.CharField(blank=True, max_length=10, null=True)),
                ('phone2', models.CharField(blank=True, max_length=10, null=True)),
                ('le', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('lo', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('image', models.ImageField(default='profile.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('scor', models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True)),
                ('idScor', models.AutoField(primary_key=True, serialize=False)),
                ('idShop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userP', models.CharField(max_length=200)),
                ('passp', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='userP',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserP'),
        ),
    ]
