from django.urls import path
from . import views

urlpatterns = [
    path('update-resume',views.update_resume,name='update-resume'), # type: ignore
    path('resume-details',views.resume_details,name='resume-details'),
]



