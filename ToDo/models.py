from django.db import models as md

# Create your models here.
class ToDo(md.Model):
    title = md.CharField(max_length=200)
    description = md.TextField(blank=True, null=True)
    created_at = md.DateTimeField(auto_now_add=True)
    completed = md.BooleanField(default=False)
    