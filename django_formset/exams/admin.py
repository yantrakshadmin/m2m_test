from django.contrib import admin

from exams.models import exams, SubExam
# Register your models here.
admin.site.register(exams)
admin.site.register(SubExam)