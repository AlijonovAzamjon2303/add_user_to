from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/')  # media/images/ papkaga saqlanadi

    def __str__(self):
        return self.name
