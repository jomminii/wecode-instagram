import json

from .models import Comment
from core.utils import login_decorator

from django.views import View
from django.http import JsonResponse, HttpResponse

class CommentView(View):
    @login_decorator
    def get(self, request):
        return JsonResponse({'comment_list':list( Comment.objects.values())},status=200)
    
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        Comment(
            email = request.user.email,
            comment = data['comment'],
        ).save()
        
        return HttpResponse(status=200)


