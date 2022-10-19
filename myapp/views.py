# Create your views here.

from django.shortcuts import render,get_object_or_404
from .models import Doctor,Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoctorSerializer,PatientSerializer

from rest_framework.views import APIView
from rest_framework import status,viewsets

# Doctor
class DoctorViewList(APIView):
    def get(self,request):
        tasks = Doctor.objects.all()
        serializer = DoctorSerializer(tasks,many=True)

        return Response({
            'status' : True,
            'message' : 'task fetched',
            'data' : serializer.data
        })

    def post(self,request):
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True,
                    'message' : 'task fetched',
                    'data' : serializer.data
                })
            #return Response({'status' : False,'message' : 'invalid data','data' : serializer.errors})
        except Exception as e:
            print(e)
        return Response({
            'status' : False,
            'message' : 'Invalid Data',
        })

# with primary key 
class DoctorViewDetail(APIView):
    def get(self, request, pk, format=None):
        task = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(task,many=False)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        task = Doctor.objects.get(pk=pk)
        task.delete()
        return Response({'message' : 'Task Deleted successfully'},status=status.HTTP_204_NO_CONTENT)

    
    def put(self, request, pk, format=None):
        task = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        task = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Patient
class PatientViewList(APIView):
    def get(self,request):
        tasks = Patient.objects.all()
        serializer = PatientSerializer(tasks,many=True)

        return Response({
            'status' : True,
            'message' : 'task fetched',
            'data' : serializer.data
        })

    def post(self,request):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True,
                    'message' : 'task fetched',
                    'data' : serializer.data
                })
            #return Response({'status' : False,'message' : 'invalid data','data' : serializer.errors})
        except Exception as e:
            print(e)
        return Response({
            'status' : False,
            'message' : 'Invalid Data',
        })

# with primary key 
class PatientViewDetail(APIView):
    def get(self, request, pk, format=None):
        task = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(task,many=False)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        task = Patient.objects.get(pk=pk)
        task.delete()
        return Response({'message' : 'Task Deleted successfully'},status=status.HTTP_204_NO_CONTENT)

    
    def put(self, request, pk, format=None):
        task = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        task = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

