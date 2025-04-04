# Generated by Django 5.1.6 on 2025-03-28 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('title_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_name', models.CharField(max_length=50)),
                ('title_code', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1, help_text='1: Active, 0: Inactive')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1, help_text='1: Active, 0: Inactive')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('department_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1, help_text='1: Active, 0: Inactive')),
            ],
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('education_id', models.AutoField(primary_key=True, serialize=False)),
                ('education_name', models.CharField(max_length=100)),
                ('education_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=100)),
                ('position_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1, help_text='1: Active, 0: Inactive')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('id_card', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('id_card_issue_date', models.DateField(blank=True, null=True)),
                ('id_card_issue_place', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('status', models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('On Leave', 'On Leave')], default='Working', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.department')),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.educationlevel')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.academictitle')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.position')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCertificate',
            fields=[
                ('certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate_name', models.CharField(max_length=200)),
                ('issued_by', models.CharField(blank=True, max_length=200, null=True)),
                ('issued_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('certificate_number', models.CharField(blank=True, max_length=100, null=True)),
                ('attachment_file', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Valid', 'Valid'), ('Expired', 'Expired'), ('Revoked', 'Revoked')], default='Valid', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.certificatetype')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('hometown_province', models.CharField(blank=True, max_length=100, null=True)),
                ('hometown_district', models.CharField(blank=True, max_length=100, null=True)),
                ('hometown_ward', models.CharField(blank=True, max_length=100, null=True)),
                ('hometown_address', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_province', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_district', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_ward', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=255, null=True)),
                ('current_province', models.CharField(blank=True, max_length=100, null=True)),
                ('current_district', models.CharField(blank=True, max_length=100, null=True)),
                ('current_ward', models.CharField(blank=True, max_length=100, null=True)),
                ('current_address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceAndTax',
            fields=[
                ('insurance_tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('social_insurance_number', models.CharField(blank=True, max_length=20, null=True)),
                ('social_insurance_date', models.DateField(blank=True, null=True)),
                ('social_insurance_place', models.CharField(blank=True, max_length=100, null=True)),
                ('health_insurance_number', models.CharField(blank=True, max_length=20, null=True)),
                ('health_insurance_date', models.DateField(blank=True, null=True)),
                ('health_insurance_place', models.CharField(blank=True, max_length=100, null=True)),
                ('health_care_provider', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_code', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
