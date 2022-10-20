from django.urls import path,include
from . import views

urlpatterns =[
    #class based APIView
    path('doctors/',views.DoctorViewList.as_view()),
    path('doctordetail/<str:pk>/',views.DoctorViewDetail.as_view()),
    path('patients/',views.PatientViewList.as_view()),
    path('patientdetail/<str:pk>/',views.PatientViewDetail.as_view()),
    path('appointments/',views.AppointmentViewList.as_view()),
    path('appointmentdetail/<str:pk>/',views.AppointmentViewDetail.as_view()),
  
]
