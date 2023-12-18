from rest_framework import serializers
from .models import ToDo

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError('Title length must not exceed 50 characters.')
        return value
