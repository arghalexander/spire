from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Job
from .forms import JobForm

# Create your views here.
def job_detail(request, job_id):
	job = get_object_or_404(Job,pk=job_id)
	return render(request, 'spiresite/job_page.html',{'job': job})


@login_required
def job_create(request):

	if request.method == 'POST':

		form = JobForm(request.POST)

		if form.is_valid():

			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('/members-directory/job-board/')
	else:
		form = JobForm()

	return render(request, 'spiresite/job_form.html', {'form': form})
