from django.db import models

class contact(models.model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True) # make message optional by adding blank=True
    submitted_at = models.DataTimeField(auto_now_add=True)
    
    def str(self):
        return f'Contact from {self.name}'
# Create your models here.
