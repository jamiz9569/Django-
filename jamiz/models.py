from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('black', 'Black'),
        ('green', 'Green'),
        ('herbal', 'Herbal'),
        ('oolong', 'Oolong'),
        ('white', 'White'),
    ]

    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_variety_images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return self.name