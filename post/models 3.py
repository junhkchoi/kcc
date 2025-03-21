from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=20, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title