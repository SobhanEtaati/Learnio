from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Students, Teachers, Classes, Student_Classes, Sessions

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'role', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):   
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    
        return user


# Students Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('student_id', 'username', 'first_name', 'last_name', 'email')


# Teachers Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('teacher_id', 'username', 'first_name', 'last_name', 'email')


# Classes Serializer
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('')


# Sessions Serializer
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = ('')


# Student_Classes Serializer
class Student_ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Classes
        fields = ('')


#Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)