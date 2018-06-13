from django.db import models
# fetching Model from models

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def ___str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name = 'Ingredients', on_delete= models.CASCADE
    )

    def __str__(self):
        return self.name

# making 2 collections i.e Category and ingredients
