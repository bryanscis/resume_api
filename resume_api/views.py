from django.http import JsonResponse
from .models import Comments
from .serializers import CommentSerializer

def comments_list(request):
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return JsonResponse({'comments': serializer.data})