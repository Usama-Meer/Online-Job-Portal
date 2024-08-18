from django.shortcuts import redirect, render
from job.models import ApplyJob

# def proxy(request):
#     if request.user.is_applicant:
#         return redirect(request, 'applicant.html')
#     elif request.user.is_recruiter:
#         return redirect(request, 'recruiter.html')
    

# #applicant dashboard
# def applicant_dashboard(request):
#     return render(request,'dashboard/applicant_dashboard.html')

# #recruiter dashboard
# def recruiter_dashboard(request):
#     return render(request,'dashboard/recruiter_dashboard.html')


def dashboard(request):
    
        
    return render(request, 'dashboard/dashboard.html')