from django.db import models
# from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

# Create your models here.
class Snacks(models.Model):
    snack_name=  models.CharField(max_length=64)
    description=  models.TextField()
    author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.snack_name
