import json
from .models import Account
from django.views import View
from django.http import JsonResponse, HttpResponse

class AccountJoinView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            email    = data['email'],
            password = data['password']
        ).save()

        # return HttpResponse(status=200)
        return JsonResponse({'message':'회원가입 완료염'},status=200)

class AccountLoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        for account in Account.objects.values():
            if account['email'] == data['email']:
                if account['password'] == data['password'] :
                    return JsonResponse({'message':'login success'},status=200)
                else :
                    return JsonResponse({'message':'login failure. wrong password'},status=200)
            
        return JsonResponse({'message':'login failure. wrong email'},status=200)