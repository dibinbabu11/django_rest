from django.shortcuts import render
from django .http import JsonResponse
from .models import Student
from.serializer import studentSerializers
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST','PUT', 'DELETE'])
def index(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=studentSerializers(student,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method=="POST":
        serializer=studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        try:
            student = Student.objects.get(pk=request.data.get('id'))
            serializer = studentSerializers(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

       
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            student = Student.objects.get(pk=request.data.get('id'))
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


    return JsonResponse()