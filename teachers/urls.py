from django.urls import path
from . import views

urlpatterns = [
    path('staff_home/', views.staff_home, name="staff_home"),
    path('staff_take_attendance/', views.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', views.get_students, name="get_students"),
    path('save_attendance_data/', views.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', views.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', views.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', views.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', views.update_attendance_data, name="update_attendance_data"),
    path('staff_apply_leave/', views.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', views.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', views.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', views.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', views.staff_profile, name="staff_profile"),
    path('staff_profile_update/', views.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', views.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', views.staff_add_result_save, name="staff_add_result_save"),
]
