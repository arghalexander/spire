from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Job

# Create your views here.
def job_detail(request, slug):
	
	job = get_object_or_404(Job, slug=slug)
	return render(request, 'spiresite/job_page.html',{'job': job})


