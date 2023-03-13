
from django.urls import path

from hospital import views

urlpatterns = [

#-------------FOR HOME VIEW RELATED URLS

    path('', views.home_view, name=''),


#-------------FOR PATIENT RELATED URLS
    path('patientclick', views.patientclick_view),
    path('patientsignup', views.patient_signup_view),


#-------------FOR ADMIN RELATED URLS
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('adminclick', views.adminclick_view),
    path('adminsignup', views.admin_signup_view),
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view, name='admin-view-doctor-view'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor-view/<int:pk>', views.update_doctor_view, name='update-doctor-view'),
    path('admin-add-doctor-view', views.admin_add_doctor_view, name='admin-add-doctor-view'),



#-------------FOR DOCTOR RELATED URLS
 path('doctorclick', views.doctorclick_view),
 path('doctorsignup', views.admin_signup_view),



]
