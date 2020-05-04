from django.db import models

# Create your models here.
class Notes(models.Model):
    tasks=models.TextField(max_length=1000)
    status=models.BooleanField(default=0,blank=True,null=True)

    def __str__(self):
        return self.tasks
