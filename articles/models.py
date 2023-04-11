from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(
        User, related_name="Article", on_delete=models.DO_NOTHING, null=True
    )
    title = models.CharField(max_length=30, null=True)
    content = models.CharField(max_length=150, null=True)
    author = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

#     def __str__(self):
#     def Add_Post(self):
#
# class Question(models.Model):
#     # ...
#     def __str__(self):
#         return self.question_text
#
# class Choice(models.Model):
#     # ...
#     def __str__(self):
#         return self.choice_text
