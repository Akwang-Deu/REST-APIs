
from django.shortcuts import render

from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from course.models import Course
from .serializers import TeacherSerializer, ClassPeriodSerializer, CourseSerializer,StudentSerializer,MinimalStudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name= request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students= students.filter(first_name=first_name)
        
        if country:
            students= students.filter(country=country)
        serializer = MinimalStudentSerializer(students, many=True)
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

    
    def enroll_student(self, student,course_id):
        course= Course.objects.get(id=course_id)
        student.course.add(course)


    def post(self, request, id):
        student= Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id=request.data.get("course")
            self.enroll_student(student,course_id)
        return Response(status=status.HTTP_201_CREATED)


        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        first_name = request.query_params.get("first_name")
        cv = request.query_params.get("cv")
        if first_name:
            students = students.filter(first_name=first_name)
        if cv:
            students = students.filter(cv=cv)
        serializer = MinimalTeacherSerializer(teachers, many=True)
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




    def assign_course(self, teacher,course_id):
        courses = Course.objects.get(id=course_id)
        teacher.courses.add(courses)


    def post(self,request, id):
        teacher= Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign":
            course_id=request.data.get("course")
            self.assign(teacher,course_id)
        return Response(status.HTTP_201_CREATED)


    def assign_class(self,teacher,class_name):
        classes = Classes.objects.get(id=id)
        teacher.Course.add(Course)

    
    def post(self,request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign":
            class_name = request.data.get("class")
            self.assign_class(teacher, class_name)
        return Response(status.HTTP_201_CREATED)



class ClassperiodListView(APIView):
    def get(self, request):
        end_time = request.query_params.get("end_time")
        start_time = request.query_params.get("start-time")
        if end_time:
            Classperiod = Classperiod.filter(first_name=end_time)
        if start_time:
            student=student.filter()
        serializer = MinimalStudentSerializer(student, many=True)
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        course =Course.objects.get()
        serializer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    
    def post (self, request, id):
        course = Course.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_teacher":
            teacher_id = request.data.get("teacher")
            teacher= Teacher.objects.get(id=teacher_id)
            course.teaches.add(teacher)
            return Response({"status": "teacher assigned"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

 
class ClassroomListView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassroomDetailView(APIView):

    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def post(self, request, id):
        classroom = Classroom.objects.get(id=id)
        action = request.data.get("action")
        if action == "add_student":
            student_id = request.data.get("student")
            student = Student.objects.get(id=student_id)
            classroom.students.add(student)
            return Response({"status": "student added"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)








        












