from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
                "id",
                "title",
                "description",
                )     # we can also use '__all__' in fields value when we want to get the all fields
        
