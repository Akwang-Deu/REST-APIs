
from django.shortcuts import render

from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from course.models import Course
from .serializers import TeacherSerializer, ClassPeriodSerializer, CourseSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetailView(APIView):
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = TeacherSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = StudentSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




class ClassperiodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = ClassPeriodSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodDetailView(APIView):
    def put(self, request, id):
        classPeriod = ClassPeriod.objects.get(id = id)
        serializer= ClassPeriodSerializer(classPeriod,data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        else:
             return Respond(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        ClassPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.get()
        serializers = CourseSerializer(course, many=True)
        return Response(serializer.data)


    def post (self, request):
        serializer = Course(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CourseDetailView(APIView):
    def put(self,reguest, id):
        course = Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=reguest.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def delete(self, request, id):
        course =Course.objects.get()
        serializer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)












