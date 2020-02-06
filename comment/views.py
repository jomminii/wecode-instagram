import json
from .models import Comments
from django.views import View
from django.http import JsonResponse, HttpResponse

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            email = data['email'],
            comment = data['comment'],
           
        ).save()
        comment_data = Comments.objects.values()
        result = []
        for comment in comment_data:
          # comment_dict = {}
          # comment_dict['email']=comment['email']
          # comment_dict['comment']=comment['comment']
          # comment_dict['created_at']=comment['created_at']
          # print(comment_dict)
          # result.append(comment_dict)
            comment_list = []
            comment_list.append(f'email : {comment["email"]}')
            comment_list.append(f'comment : {comment["comment"]}')
            comment_list.append(f'created_at : {comment["created_at"]}')
            
            result.append(comment_list)

      # return JsonResponse({'comment_list':result},status=200)
        return JsonResponse({'comment_list':result},status=200)
    
