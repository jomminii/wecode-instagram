import jwt
import json
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY
from account.models import Account

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
            user = Account.objects.get(email=payload['email'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)
    
        except Account.DoesNotExist:  # import 한건 ObjectDoesNotExist 지만 그렇게 쓰면 attribute error 남
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        except KeyError :
            return JsonResponse({'message' : 'INVALID_KEYS' }, status=400)

        # 테스트 해보고 에러 추가

        return func(self, request, *args, **kwargs)
    
    return wrapper
