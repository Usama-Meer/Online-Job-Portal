from django.shortcuts import render,redirect
from django.contrib import messages

from users.models import User
from .form import CreateJobForm, UpdateJobForm
from .models import Job


#create a job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var=form.save(commit=True)
                var.user=request.user
                var.company=request.user.company
                var.save()

                messages.info(request,'New job has been added successfully.')
                return redirect('dashboard')
            else:
                messages.warning(request,'Something went wrong!')
                return redirect('create-job')
            
        else:
            form=CreateJobForm()
            context={'form':form}
            return render(request,'job/create_job.html',context)
        
    else:
        messages.warning(request,'Permission denied')
        return redirect('dashboard')

# update job info.
def update_job(request,pk):
    job=Job.objects.get(pk=pk)
    if request.user.is_recruiter and request.user.has_company and request.user.email==job.user.email:
        if request.method == 'POST':
            form = UpdateJobForm(request.POST,instance=job)
            if form.is_valid():
                form.save()

                messages.info(request,'Your job info has been updated!')
                return redirect('dashboard')
                
            else:
                messages.warning(request,'Something went wrong!')
                return redirect('dashboard')
            
        else:
            form=UpdateJobForm(instance=job)
            context={'form':form}
            return render(request,'job/update_job.html',context)
        
    else:
        messages.warning(request,'Permission denied')
        return redirect('dashboard')
