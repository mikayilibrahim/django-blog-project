from django.db import models
from autoslug import AutoSlugField
from blog.models import KateqoriyaModel
from  django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.models.abstract_models import DateAbstractModels


class YaziModels(DateAbstractModels):
    basliq = models.CharField( max_length=50)
    sekil = models.ImageField( upload_to='yazi_sekilleri')
    meqale = RichTextField()
   
    slug = AutoSlugField(populate_from= "basliq",unique=True)
    kateqoriyalar = models.ManyToManyField(KateqoriyaModel ,related_name="yazi")
    yazar = models.ForeignKey("account.CustomUserModel", on_delete= models.CASCADE, related_name="yazilar")

    class Meta:
        verbose_name = "Yazi"
        verbose_name_plural = "Yazi"
        db_table = "Yazi"