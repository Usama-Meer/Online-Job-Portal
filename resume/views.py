from django.shortcuts import render,redirect
from django.contrib import messages

from .form import UpdateResumeForm
from .models import Resume
from users.models import User


def update_resume(request):
    if request.user.is_applicant:
        resume=Resume.objects.get(user=request.user)
        if request.method=="POST":
            form=UpdateResumeForm(request.POST,instance=resume)
            if form.is_valid():
                var=form.save()
                user=User.objects.get(pk=request.user.id)
                user.has_resume=True
                var.save()
                user.save()
                messages.info(request,"Your resume has been updated. You can apply for jobs.")
                return redirect('dashboard')
            else:
                messages.warning(request,'Something went wrong!')
        else:
            form=UpdateResumeForm(instance=resume)
            context={'form':form}
            return render(request,'resume/update_resume.html',context)
        
    else:
        messages.warning(request,'Permission denied')
        return redirect('dashboard')
    


#resume detail function

def resume_details(request,pk):
    resume=Resume.objects.get(pk=pk)
    context={'resume':resume}
    return render(request,'resume/resume_details.html',context)

# Create your views here.
