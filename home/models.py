from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Commentdc(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
class Commentac(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class CommentRE(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
class CommentHE(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
# class CommentA(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     context = models.TextField()
#     dates = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.user)
    
class CommentMS(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class CommentAI(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)