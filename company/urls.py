from django.urls import path
from . import views

urlpatterns = [

    path('company-details/<int:pk>',views.company_details,name='company-details'),
    path('update-company/',views.update_company, name='update-company'), # type: ignore
]
