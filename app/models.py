from django.db import models
from django.urls import reverse
import uuid # Required for Suit
# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, help_text="question")
    # suit =  models.ForeignKey('Suit', on_delete=models.SET_NULL,null=True, help_text="my suit")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.question

class Suit(models.Model):
    id = models.AutoField(primary_key=True)
    q1 = models.ForeignKey('Question', on_delete=models.SET_NULL,null=True,related_name="q1", help_text="question1")
    q2 = models.ForeignKey('Question', on_delete=models.SET_NULL,null=True,related_name="q2", help_text="question2")
    q3 = models.ForeignKey('Question', on_delete=models.SET_NULL,null=True,related_name="q3", help_text="question3")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s' % (self.id)
