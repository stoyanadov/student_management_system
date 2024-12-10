from django.urls import path
from .views import StudentHomeView, StudentViewAttendanceView, StudentViewAttendancePostView, StudentApplyLeaveView, \
StudentApplyLeaveSaveView, StudentFeedbackView, StudentFeedbackSaveView, StudentProfileView, StudentProfileUpdateView, \
StudentViewResultView

urlpatterns = [
    path('student_home/', StudentHomeView.as_view(), name="student_home"),
    path('student_view_attendance/', StudentViewAttendanceView.as_view(), name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViewAttendancePostView.as_view(),
         name="student_view_attendance_post"),
    path('student_apply_leave/', StudentApplyLeaveView.as_view(), name="student_apply_leave"),
    path('student_apply_leave_save/', StudentApplyLeaveSaveView.as_view(), name="student_apply_leave_save"),
    path('student_feedback/', StudentFeedbackView.as_view(), name="student_feedback"),
    path('student_feedback_save/', StudentFeedbackSaveView.as_view(), name="student_feedback_save"),
    path('student_profile/', StudentProfileView.as_view(), name="student_profile"),
    path('student_profile_update/', StudentProfileUpdateView.as_view(), name="student_profile_update"),
    path('student_view_result/', StudentViewResultView.as_view(), name="student_view_result"),
]