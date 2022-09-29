from django.db import models
from django.contrib.auth.models import User
from blog.models import YaziModels
from blog.models.abstract_models import DateAbstractModels
class  YorumModel(DateAbstractModels):
    yazan = models.ForeignKey("account.CustomUserModel", on_delete=models.CASCADE,related_name="yorum")
    yazi = models.ForeignKey(YaziModels, on_delete=models.CASCADE ,related_name="yorumlar")
    yorum = models.TextField()
   


    class Meta:
        db_table = "yorum"
        verbose_name = "şərh"



    def __str__(self):
        return self.yazan.username
    

    

 