from django.http import JsonResponse, HttpResponse
from .models import Comments, Projects, Experience, Contact, Route
from .serializers import CommentSerializer, ProjectsSerializer, ExperienceSerializer, ContactSerializer, RouteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def comments_list(request):

    if request.method == 'GET':
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse({'comments': serializer.data})
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid Parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def projects_list(request):

    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse({'projects': serializer.data})
    
@api_view(['GET'])
def experience_list(request):

    if request.method == 'GET':
        projects = Experience.objects.all()
        serializer = ExperienceSerializer(projects, many=True)
        return JsonResponse({'experience': serializer.data})
    
@api_view(['GET'])
def contact_list(request):

    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return JsonResponse({'contact': serializer.data})
    
@api_view(['GET'])
def homepage(request):
    if request.method == 'GET':
        return JsonResponse({'Check out my resume!': 'Add /routes to see all possible API routes.'})
    
@api_view(['GET'])
def routes_list(request):
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return JsonResponse({'routes': serializer.data})