from django.db import models

# Create your models here.

class sampleTable(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150, default="", blank=True)
    phone = models.CharField(max_length=10, default="", blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
       return self.user_name

class categoryTable(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class dressinfoTable(models.Model):
    id = models.AutoField(primary_key=True)
    dress_name = models.CharField(max_length=200)
    dress_image = models.URLField(max_length=4000)
    dress_price = models.CharField(max_length=50)
    category = models.name = models.ForeignKey('categoryTable', on_delete=models.CASCADE)

    def __str__(self):
        return self.dress_name


