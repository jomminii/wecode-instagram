from django.db import models

class SearchList(models.Model):
    post_title = models.CharField(max_length = 200)
    posting_date = models.CharField(max_length = 100)
    blog_url = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'search_lists'
