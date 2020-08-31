from django.db import models

# Create your models here.
LANGUAGES = [("en","En"),("sr","Sr")]

class Quote(models.Model):
    quote = models.TextField()
    auther = models.CharField(max_length=250)
    source = models.CharField(max_length=99,null=True)
    rating = models.CharField(max_length=99, null=True,blank=True)
    language = models.CharField(max_length=20, choices=LANGUAGES,default="en")


    # def __str__(self):
    #     return str(self.auther+self.language)