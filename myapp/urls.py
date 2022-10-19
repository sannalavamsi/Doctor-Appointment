from django.urls import path,include
from . import views





urlpatterns =[
    #class based APIView
    path('doctor/',views.DoctorViewList.as_view()),
    path('doctordetail/<str:pk>/',views.DoctorViewDetail.as_view()),
    path('patient/',views.PatientViewList.as_view()),
    path('patientdetail/<str:pk>/',views.PatientViewDetail.as_view()),
  
]

