from rest_framework import serializers
from main_app.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'admin', 'course_id', 'session_year_id', 'address']
