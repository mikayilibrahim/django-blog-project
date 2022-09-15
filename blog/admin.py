from django.contrib import admin
from blog.models import KateqoriyaModel,YaziModels

admin.site.register(KateqoriyaModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('basliq','meqale4')
    list_display = ( 
        'basliq',
        'meqale',
        'yaradilma_tarix'
        
        
        )

admin.site.register(YaziModels,YazilarAdmin)