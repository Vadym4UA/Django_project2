from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from drf_yasg.utils import swagger_auto_schema

class CategoryListCreateView(APIView):
    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(APIView):
    @swagger_auto_schema(responses={200: TaskSerializer(many=True)})
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    @swagger_auto_schema(responses={200: TaskSerializer()})
    def get(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)