from django.core.management.base import BaseCommand, CommandError
from exams.models import exams
import pysolr

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        exams1 = exams.objects.all()
        solr = pysolr.Solr('http://127.0.0.1:8983/solr/new_core1')
        iexam = []
        for exam in exams1:
            iexam.append({"id": exam.id,"name": exam.name})
        print(iexam)
        solr.add(iexam, commit="True")