from django.db import models

# Create your models here.

class Job(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    description=models.CharField(max_length=500)
    qualification=models.CharField(max_length=500)
    banner=models.ImageField()
    date_posted=models.DateTimeField(auto_now_add=True)
    expired=models.BooleanField(default=False)
    other_info=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

