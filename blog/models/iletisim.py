from django.db import models


class IletisimModel(models.Model):

    email= models.EmailField(max_length=250)
    ad_soyad = models.CharField(max_length=150)
    yorum = models.TextField()
    yaradilma_tarixi = models.DateTimeField(auto_now_add = True)
    

    class Meta:
        db_table = "iletisim"
        verbose_name = "İletişim"
        

    def __str__(self):
        return self.email

