import json

from .models import Comment

from django.views import View
from django.http import JsonResponse, HttpResponse

class CommentView(View):
    def get(self, request):
        comment_data = Comment.objects.values()
        result = []
        
        for comment in comment_data:
            comment_dict = {
                'email' : comment['email'],
                'comment' : comment['comment'],
                'created_at' : comment['created_at']
            }
            
            result.append(comment_dict)
            
        return JsonResponse({'comment_list':result},status=200)

    def post(self, request):
        data = json.loads(request.body)

        Comment(
            email = data['email'],
            comment = data['comment'],
        ).save()
        
        return HttpResponse(status=200)


