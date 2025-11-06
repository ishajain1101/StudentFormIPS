from django.contrib import admin
from .models import StudentInquiry

@admin.register(StudentInquiry)
class StudentInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'student_name','dob','father_name','father_mobile','mobile', 'email', 'course',
        'category', 'gender', 'city','address', 'created_at'
    )
    
