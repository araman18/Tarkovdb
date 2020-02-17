from django.db import models


class Item(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    def __str__ (self):
    	return self.name
    	
    def expensive(self):
    	if(self.price > 1000000):
    		return "Yah"
    	else:
    		return "Nah"

