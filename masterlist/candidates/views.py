from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Candidate, CandidateTable

@login_required
def table(request):
    table = CandidateTable(Candidate.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'candidates.html', {'table': table})
