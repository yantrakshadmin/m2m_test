from django.forms import ModelForm
from exams.models import exams, SubExam

class ExamForm(ModelForm):
	class Meta:
		model = exams
		fields = '__all__'


class SubExamForm(ModelForm):
	class Meta:
		model = SubExam
		exclude = ["parent_exam"]