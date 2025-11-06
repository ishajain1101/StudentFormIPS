from django.db import models

class StudentInquiry(models.Model):
    # Basic Information
    student_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    CATEGORY_CHOICES = [
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('General', 'General'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=True, blank=True)

    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    COURSE_CHOICES = [
        ('BBA', 'BBA'),
        ('BCom', 'BCom'),
        ('BCA', 'BCA'),
        ('BA.LL.B(Hon)', 'BA.LL.B(Hon)'),
        ('MBA', 'MBA'),
        ('MCA', 'MCA'),
        ('LL.B(Hon)', 'LL.B(Hon)'),
    ]
    course = models.CharField(max_length=30, choices=COURSE_CHOICES, null=True, blank=True)

    # Family Information
    father_name = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    annual_income = models.CharField(max_length=50, null=True, blank=True)
    father_mobile = models.CharField(max_length=15, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)

    # Address
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    # Academic Info
    x_percent = models.CharField(max_length=10, null=True, blank=True)
    x_year = models.CharField(max_length=10, null=True, blank=True)
    x_board = models.CharField(max_length=50, null=True, blank=True)

    xii_stream_percent = models.CharField(max_length=100, null=True, blank=True)
    xii_year = models.CharField(max_length=10, null=True, blank=True)
    xii_board = models.CharField(max_length=50, null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)

    grad_stream_percent = models.CharField(max_length=100, null=True, blank=True)
    college_name = models.CharField(max_length=200, null=True, blank=True)
    university_name = models.CharField(max_length=200, null=True, blank=True)

    # Source of Information
    src_website = models.BooleanField(default=False)
    src_newspaper = models.BooleanField(default=False)
    src_hoarding = models.BooleanField(default=False)
    src_calling = models.BooleanField(default=False)
    src_ads = models.BooleanField(default=False)
    src_other = models.BooleanField(default=False)
    src_other_text = models.CharField(max_length=200, null=True, blank=True)

    # Verification
    verified_by = models.CharField(max_length=100, null=True, blank=True)
    remark = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.student_name} ({self.course})"
