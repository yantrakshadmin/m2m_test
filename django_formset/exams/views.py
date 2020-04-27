from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.http import HttpResponse

from exams.models import exams, SubExam
from exams.forms import ExamForm, SubExamForm
# Create your views here.
import pysolr


class dashboard(ListView):
    model = exams
    template_name = 'exams/exam_dashboard.html'

    def get_queryset(self):
        context = exams.objects.all()
        q = self.request.GET.get('q')

        if q:
            solr = pysolr.Solr('http://127.0.0.1:8983/solr/new_core1')
            myquery = 'name:' + q
            results = solr.search(q=myquery)
            return results

        return context


def exam_add(request):
    exform = ExamForm()
    subexformset = modelformset_factory(SubExam, form=SubExamForm, extra=1)
    subexformset = subexformset(request.POST or None, queryset=SubExam.objects.filter(id__isnull=True))
    if request.method == 'POST':
        exam = exams()
        exform = ExamForm(request.POST, instance=exam)
        if exform.is_valid() and subexformset.is_valid():
            exform.save()
            instances = subexformset.save(commit=False)
            for subexform in instances:
                subexform.parent_exam = exam.id
                subexform.save()
            return redirect('/exams/dashboard/')
        else:
            print('invalid data')

    return render(request, 'exams/exam_create.html', {'exform': exform, 'exformset': subexformset})


def exam_edit(request, pk=None):
    exam = exams.objects.get(id=pk)
    exform = ExamForm(instance=exam)
    subexformmodelset = modelformset_factory(SubExam, form=SubExamForm)
    subexformset = subexformmodelset(request.POST or None, queryset=SubExam.objects.filter(parent_exam=pk))
    if request.method == 'POST':
        exform = ExamForm(request.POST, instance=exam)
        if exform.is_valid() and subexformset.is_valid():
            exform.save()
            instances = subexformset.save(commit=False)
            for subexform in instances:
                subexform.parent_exam = exam.id
                subexform.save()
            return redirect('/exams/dashboard/')
        else:
            print(subexformset.errors)

    return render(request, 'exams/exam_create.html', {'exform': exform, 'exformset': subexformset})


def getset(request):
    extras = int(request.GET.get('extra'))
    pk = int(request.GET.get('pk'))
    subexformset = modelformset_factory(SubExam, form=SubExamForm, extra=extras)
    subexformset = subexformset(request.POST or None, queryset=SubExam.objects.filter(parent_exam=pk))
    subexformset = [form for form in subexformset]
    subexformset = subexformset[-1]
    return render(request, 'exams/formset_partial.html', {'form': subexformset})


def sub_delete(request, sub_id=None):
    if sub_id:
        SubExam.objects.get(id=sub_id).delete()
    else:
        print('not deleted')
    return HttpResponse('deleted')
