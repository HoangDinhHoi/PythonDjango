from django.db import models

# Create your models here.
class PriceMenu(models.Model):
    name = models.CharField(max_length=50) # exmaple: make, cut, color
    price = models.FloatField(max_length=50) # ex: 50000VND
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    pricemenu_image = models.ImageField(upload_to='pricemenu_image/', null=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
