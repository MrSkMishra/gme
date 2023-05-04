from django.db import models

# Create your models here.
class PalindromeGamez(models.Model):
    word = models.CharField(max_length=100)
    is_palindrome = models.BooleanField(default=False)


    def __str__(self) :
        return self.word