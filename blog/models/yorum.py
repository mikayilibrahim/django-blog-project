from django.db import models
from django.contrib.auth.models import User
from blog.models import YaziModels

class  YorumModel(models.Model):
    yazan = models.ForeignKey(User, on_delete=models.CASCADE,related_name="yorum")
    yazi = models.ForeignKey(YaziModels, on_delete=models.CASCADE ,related_name="yorumlar")
    yorum = models.TextField()
    yaradilma_tarixi = models.DateTimeField(auto_now_add = True)
    deyisdirilme_tarixi = models.DateTimeField(auto_now= True)


    class Meta:
        db_table = "yorum"
        verbose_name = "şərh"



    def __str__(self):
        return self.yazan.username
    

    

 