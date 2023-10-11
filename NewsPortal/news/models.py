from django.db import models
from django.core.validators import MinValueValidator
 
 
# Создаём модель новости
class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, 
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', 
    )
   
 
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
 
 
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 
 
    def __str__(self):
        return f'{self.name.title()}'