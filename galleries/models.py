from django.db import models

# Create your models here.
class StyleImage(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length = 500)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='style_image/')

    def __unicode__(self):
        return self.title
    def __repr__(self):
        return self.title