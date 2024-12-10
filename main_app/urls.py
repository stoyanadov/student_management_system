from django.urls import path
from . import views
from .views import LoginPageView, RegisterView, LoginView, LogoutView, AdminHomeView, AddStaffView, AddStaffSaveView, \
    ManageStaffView, StudentListCreateAPIView

urlpatterns = [
    path('', LoginPageView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('doLogin/', LoginView.as_view(), name="doLogin"),
    path('logout_user/', LogoutView.as_view(), name="logout_user"),
    path('admin_home/', AdminHomeView.as_view(), name="admin_home"),
    path('add_staff/', AddStaffView.as_view(), name="add_staff"),
    path('add_staff_save/', AddStaffSaveView.as_view(), name="add_staff_save"),
    path('manage_staff/', ManageStaffView.as_view(), name="manage_staff"),
    path('edit_staff/<staff_id>/', views.edit_staff, name="edit_staff"),
    path('edit_staff_save/', views.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', views.delete_staff, name="delete_staff"),
    path('add_course/', views.add_course, name="add_course"),
    path('add_course_save/', views.add_course_save, name="add_course_save"),
    path('manage_course/', views.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', views.edit_course, name="edit_course"),
    path('edit_course_save/', views.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', views.delete_course, name="delete_course"),
    path('manage_session/', views.manage_session, name="manage_session"),
    path('add_session/', views.add_session, name="add_session"),
    path('add_session_save/', views.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', views.edit_session, name="edit_session"),
    path('edit_session_save/', views.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', views.delete_session, name="delete_session"),
    path('add_student/', views.add_student, name="add_student"),
    path('add_student_save/', views.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', views.edit_student, name="edit_student"),
    path('edit_student_save/', views.edit_student_save, name="edit_student_save"),
    path('manage_student/', views.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', views.delete_student, name="delete_student"),
    path('add_subject/', views.add_subject, name="add_subject"),
    path('add_subject_save/', views.add_subject_save, name="add_subject_save"),
    path('manage_subject/', views.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', views.edit_subject, name="edit_subject"),
    path('edit_subject_save/', views.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', views.delete_subject, name="delete_subject"),
    path('check_email_exist/', views.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', views.check_username_exist, name="check_username_exist"),
    path('student_feedback_message/', views.student_feedback_message, name="student_feedback_message"),
    path('student_feedback_message_reply/', views.student_feedback_message_reply, name="student_feedback_message_reply"),
    path('staff_feedback_message/', views.staff_feedback_message, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', views.staff_feedback_message_reply, name="staff_feedback_message_reply"),
    path('student_leave_view/', views.student_leave_view, name="student_leave_view"),
    path('student_leave_approve/<leave_id>/', views.student_leave_approve, name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', views.student_leave_reject, name="student_leave_reject"),
    path('staff_leave_view/', views.staff_leave_view, name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', views.staff_leave_approve, name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', views.staff_leave_reject, name="staff_leave_reject"),
    path('admin_view_attendance/', views.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates/', views.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', views.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', views.admin_profile, name="admin_profile"),
    path('admin_profile_update/', views.admin_profile_update, name="admin_profile_update"),
    path('api/', StudentListCreateAPIView.as_view(), name='student_list_create_api'),
]