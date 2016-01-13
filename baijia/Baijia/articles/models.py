from django.db import models

# Create your models here.

class Author(models.Model):
    auth_name = models.CharField(max_length=20)
    classification = models.CharField(max_length=20)

    def __str__(self):
        return self.auth_name.encode('utf-8') 


class articles(models.Model):
    article_title = models.CharField(max_length = 100)
    article_abstract = models.CharField(max_length = 500)
    article_href = models.CharField(max_length = 100)
    pic_href = models.CharField(max_length = 200)
    auth_id = models.ForeignKey(Author)

    def __str__(self):
        return self.article_title.encode('utf-8')
