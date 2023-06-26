from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(max_length=20)
    # image=models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name
    
class course(models.Model):
    course=models.CharField(max_length=100)
    time=models.TimeField
    Person=models.ForeignKey(person,on_delete=models.CASCADE)

    def __str__(self):
        return self.course
    
class Image(models.Model):
    img = models.ImageField(upload_to='images')
    
class Cart(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

    def __str__(self):
        return self.item_name
