from rest_framework import serializers
from .models import Comments, Projects, Experience

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'first_name', 'last_name', 'email', 'comment', 'created_at']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'time_at_company', 'responsibilities']