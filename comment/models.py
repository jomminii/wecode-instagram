from django.db import models

class Comments(models.Model):
    email = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'

        

