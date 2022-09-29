from  django.db import models


class DateAbstractModels(models.Model):
    yaradilma_tarix = models.DateTimeField( auto_now_add=True)
    deyisdirilme_tarixi = models.DateTimeField(auto_now=True)

    

    class Meta:
        abstract = True
    