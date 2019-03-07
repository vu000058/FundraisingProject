# Generated by Django 2.1.5 on 2019-03-07 04:39

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
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500, null=True)),
                ('raised_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('deducted_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundraisingGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('term', models.CharField(max_length=10)),
                ('event', models.CharField(max_length=100)),
                ('event_due', models.DateField(auto_now_add=True)),
                ('agency', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True)),
                ('due_date', models.DateField(null=True)),
                ('delegator', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=20)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.Section')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_instructor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('activation_code', models.CharField(max_length=100, null=True)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='webapp.Section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fundraisinggoal',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='webapp.Section'),
        ),
        migrations.AddField(
            model_name='donation',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='webapp.FundraisingGoal'),
        ),
    ]
