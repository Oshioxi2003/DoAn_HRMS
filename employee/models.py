from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1, help_text='1: Active, 0: Inactive')
    
    def __str__(self):
        return self.department_name

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100)
    position_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1, help_text='1: Active, 0: Inactive')
    
    def __str__(self):
        return self.position_name

class AcademicTitle(models.Model):
    title_id = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=50)
    title_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1, help_text='1: Active, 0: Inactive')
    
    def __str__(self):
        return self.title_name

class EducationLevel(models.Model):
    education_id = models.AutoField(primary_key=True)
    education_name = models.CharField(max_length=100)
    education_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.education_name

class Employee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('Working', 'Working'),
        ('Resigned', 'Resigned'),
        ('On Leave', 'On Leave'),
    )
    
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    id_card = models.CharField(max_length=20, unique=True, null=True, blank=True)
    id_card_issue_date = models.DateField(null=True, blank=True)
    id_card_issue_place = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    education = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.ForeignKey(AcademicTitle, on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Working')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name

class EmployeeLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    hometown_province = models.CharField(max_length=100, null=True, blank=True)
    hometown_district = models.CharField(max_length=100, null=True, blank=True)
    hometown_ward = models.CharField(max_length=100, null=True, blank=True)
    hometown_address = models.CharField(max_length=255, null=True, blank=True)
    permanent_province = models.CharField(max_length=100, null=True, blank=True)
    permanent_district = models.CharField(max_length=100, null=True, blank=True)
    permanent_ward = models.CharField(max_length=100, null=True, blank=True)
    permanent_address = models.CharField(max_length=255, null=True, blank=True)
    current_province = models.CharField(max_length=100, null=True, blank=True)
    current_district = models.CharField(max_length=100, null=True, blank=True)
    current_ward = models.CharField(max_length=100, null=True, blank=True)
    current_address = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Location for {self.employee.full_name}"
    
class InsuranceAndTax(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    
    insurance_tax_id = models.AutoField(primary_key=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    social_insurance_number = models.CharField(max_length=20, null=True, blank=True)
    social_insurance_date = models.DateField(null=True, blank=True)
    social_insurance_place = models.CharField(max_length=100, null=True, blank=True)
    health_insurance_number = models.CharField(max_length=20, null=True, blank=True)
    health_insurance_date = models.DateField(null=True, blank=True)
    health_insurance_place = models.CharField(max_length=100, null=True, blank=True)
    health_care_provider = models.CharField(max_length=100, null=True, blank=True)
    tax_code = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Insurance & Tax for {self.employee.full_name}"
    

class CertificateType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1, help_text='1: Active, 0: Inactive')
    
    def __str__(self):
        return self.type_name

class EmployeeCertificate(models.Model):
    STATUS_CHOICES = (
        ('Valid', 'Valid'),
        ('Expired', 'Expired'),
        ('Revoked', 'Revoked'),
    )
    
    certificate_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200, null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    certificate_number = models.CharField(max_length=100, null=True, blank=True)
    attachment_file = models.FileField(upload_to='certificates/', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Valid')
    
    def __str__(self):
        return f"{self.employee.full_name} - {self.certificate_name}"