from django.contrib import admin
from blog.models import KateqoriyaModel,YaziModels,YorumModel,IletisimModel

admin.site.register(KateqoriyaModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('basliq',"meqale")
    list_display = ( 'basliq','meqale','yaradilma_tarix')

admin.site.register(YaziModels,YazilarAdmin)


class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan','yaradilma_tarixi')
    
admin.site.register(YorumModel,YorumAdmin)


class IletisimAdmin(admin.ModelAdmin):
    search_fields = ("email","ad_soyad")
    list_display = ("email","ad_soyad")
    
    

admin.site.register(IletisimModel,IletisimAdmin)






