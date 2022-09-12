from django.db import models
from autoslug import AutoSlugField
from blog.models import KateqoriyaModel
from  django.contrib.auth.models import User


class YaziModels(models.Model):
    basliq = models.CharField( max_length=50,null=True,blank=True)
    sekil = models.ImageField( upload_to=("yazi_sekilleri"))
    meqale = models.TextField()
    yaradilma_tarix = models.DateTimeField( auto_now_add=True)
    deyisdirilme_tarixi = models.DateField(auto_now=True)
    slug = models.SlugField(populate_from = " basliq",unique=True)
    kateqoriyalar = models.ManyToManyField(KateqoriyaModel() ,related_name="yazi")
    yazar = models.ForeignKey(User, on_delete= models.CASCADE, related_name="yazilar")

    class Meta:
        verbose_name = "Yazi"
        verbose_name_plural = "Yazilar"
        db_name = "Yazi"