from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here


class Reviews(models.Model):
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    image=models.ImageField(upload_to='pics',null=True,blank=True)
    body = models.TextField()
    criticR = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

