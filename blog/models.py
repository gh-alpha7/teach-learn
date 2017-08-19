from django.db import models


class homepage(models.Model):
    topic=models.CharField(max_length=250)

    def __str__(self):
        return self.topic

class code(models.Model):
    topic= models.CharField(max_length=250)
    ids=models.IntegerField()
    question=models.CharField(max_length=1000)

    def __int__(self):
        return self.ids
    def publish(self):
        self.save()
    
class answ(models.Model):
    topic=models.CharField(max_length=250)
    ques=models.CharField(max_length=10000)
    user_name=models.CharField(max_length=250)
    answer=models.CharField(max_length=10000)

    def __str__(self):
        return self.topic
    
