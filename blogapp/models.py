from django.db import models

# Create your models here.
class Blog(models.Model):  
    title= models.CharField(max_length=20)  
    description= models.CharField(max_length=100)  
    author_name = models.CharField(max_length=20)  
    date= models.DateField()  
    class Meta:  
        db_table = "blog"  