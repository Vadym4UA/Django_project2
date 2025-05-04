from rest_framework import serializers
from .models import Category, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=True
    )
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'priority', 
                 'status', 'created_at', 'category', 'category_id']