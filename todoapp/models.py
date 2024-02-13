from django.db import models

# Create your models here.
class Schedule(models,Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    options=(
        ("completed","completed")
        ("not complete","not complete")
    )
    status=models.CharField(max_lenth=200,choices=options,default="not complete")
    user=models.CharField(max_field=200)

    def __str__(self):
        return self.title
