# Generated by Django 5.1.6 on 2025-03-28 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('kpi_id', models.AutoField(primary_key=True, serialize=False)),
                ('kpi_name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('min_target', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_target', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('weight_factor', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('kpi_type', models.CharField(choices=[('Individual', 'Individual'), ('Department', 'Department'), ('Company', 'Company')], default='Individual', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RewardsAndDisciplinary',
            fields=[
                ('rad_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Reward', 'Reward'), ('Disciplinary', 'Disciplinary')], max_length=20)),
                ('content', models.TextField()),
                ('decision_date', models.DateField()),
                ('decision_number', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='rewards_disciplinary/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('decided_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='decisions_made', to='employee.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEvaluation',
            fields=[
                ('evaluation_id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('result', models.DecimalField(decimal_places=2, max_digits=10)),
                ('target', models.DecimalField(decimal_places=2, max_digits=10)),
                ('achievement_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('evaluation_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('evaluated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluations_given', to='employee.employee')),
                ('kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.kpi')),
            ],
            options={
                'unique_together': {('employee', 'kpi', 'month', 'year')},
            },
        ),
    ]
