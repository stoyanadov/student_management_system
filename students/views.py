from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import datetime
from django.views import View
from django.views.generic import TemplateView

from main_app.models import CustomUser, Courses, Subjects, Students, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent, StudentResult


class StudentHomeView(TemplateView):
    template_name = "student_template/student_home_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student_obj = get_object_or_404(Students, admin=self.request.user)

        total_attendance = AttendanceReport.objects.filter(student_id=student_obj).count()
        attendance_present = AttendanceReport.objects.filter(student_id=student_obj, status=True).count()
        attendance_absent = AttendanceReport.objects.filter(student_id=student_obj, status=False).count()

        course_obj = get_object_or_404(Courses, id=student_obj.course_id.id)
        total_subjects = Subjects.objects.filter(course_id=course_obj).count()

        subject_name = []
        data_present = []
        data_absent = []

        subject_data = Subjects.objects.filter(course_id=student_obj.course_id)

        for subject in subject_data:
            # Get attendance data for the subject
            attendance = Attendance.objects.filter(subject_id=subject.id)
            attendance_present_count = AttendanceReport.objects.filter(
                attendance_id__in=attendance, status=True, student_id=student_obj.id).count()
            attendance_absent_count = AttendanceReport.objects.filter(
                attendance_id__in=attendance, status=False, student_id=student_obj.id).count()

            subject_name.append(subject.subject_name)
            data_present.append(attendance_present_count)
            data_absent.append(attendance_absent_count)

        context.update({
            "total_attendance": total_attendance,
            "attendance_present": attendance_present,
            "attendance_absent": attendance_absent,
            "total_subjects": total_subjects,
            "subject_name": subject_name,
            "data_present": data_present,
            "data_absent": data_absent
        })

        return context


class StudentViewAttendanceView(TemplateView):
    template_name = "student_template/student_view_attendance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = Students.objects.get(admin=self.request.user)
        course = student.course_id

        subjects = Subjects.objects.filter(course_id=course)

        context['subjects'] = subjects
        return context


class StudentViewAttendancePostView(View):
    def post(self, request, *args, **kwargs):
        subject_id = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        try:
            start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format")
            return redirect('student_view_attendance')

        subject_obj = Subjects.objects.get(id=subject_id)

        user_obj = CustomUser.objects.get(id=request.user.id)
        student_obj = Students.objects.get(admin=user_obj)

        # Get attendance data within the specified date range
        attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse, end_date_parse),
                                               subject_id=subject_obj)

        # Get the attendance reports for the student within the specified date range
        attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=student_obj)

        context = {
            "subject_obj": subject_obj,
            "attendance_reports": attendance_reports
        }

        return render(request, 'student_template/student_attendance_data.html', context)


class StudentApplyLeaveView(View):
    def get(self, request, *args, **kwargs):
        student_obj = Students.objects.get(admin=request.user.id)
        leave_data = LeaveReportStudent.objects.filter(student_id=student_obj)
        context = {
            "leave_data": leave_data
        }
        return render(request, 'student_template/student_apply_leave.html', context)


class StudentApplyLeaveSaveView(View):
    def post(self, request, *args, **kwargs):
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_obj = Students.objects.get(admin=request.user.id)
        try:
            leave_report = LeaveReportStudent(student_id=student_obj, leave_date=leave_date,
                                              leave_message=leave_message, leave_status=0)
            leave_report.save()
            messages.success(request, "Applied for Leave.")
            return redirect('student_apply_leave')
        except:
            messages.error(request, "Failed to Apply Leave")
            return redirect('student_apply_leave')


class StudentFeedbackView(View):
    def get(self, request, *args, **kwargs):
        student_obj = Students.objects.get(admin=request.user.id)
        feedback_data = FeedBackStudent.objects.filter(student_id=student_obj)
        context = {
            "feedback_data": feedback_data
        }
        return render(request, 'student_template/student_feedback.html', context)


class StudentFeedbackSaveView(View):
    def post(self, request, *args, **kwargs):
        feedback = request.POST.get('feedback_message')
        student_obj = Students.objects.get(admin=request.user.id)

        try:
            add_feedback = FeedBackStudent(student_id=student_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('student_feedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('student_feedback')


class StudentProfileView(View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        student = Students.objects.get(admin=user)

        context = {
            "user": user,
            "student": student
        }
        return render(request, 'student_template/student_profile.html', context)


class StudentProfileUpdateView(View):
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password and password.strip() != "":
                customuser.set_password(password)
            customuser.save()

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')


class StudentViewResultView(View):
    def get(self, request, *args, **kwargs):
        student = Students.objects.get(admin=request.user.id)
        student_result = StudentResult.objects.filter(student_id=student.id)
        context = {
            "student_result": student_result,
        }
        return render(request, "student_template/student_view_result.html", context)
