from  django.db import models
from autoslug import AutoSlugField

class KateqoriyaModel(models.Model):
    ad= models.CharField( max_length=50,blank=False,null=False)
    slug = AutoSlugField(populate_from= "ad",unique=True)

    class Meta:
        db_table = "kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
    def __str__(self):
        return self.ad
        

    