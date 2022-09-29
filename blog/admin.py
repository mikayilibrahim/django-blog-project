from django.contrib import admin
from blog.models import KateqoriyaModel,YaziModels,YorumModel,IletisimModel

admin.site.register(KateqoriyaModel)
@admin.register(YaziModels)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('basliq',"meqale")
    list_display = ( 'basliq','meqale','yaradilma_tarix')




@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan','yaradilma_tarix')
    


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ("email","ad_soyad")
    list_display = ("email","ad_soyad")
    
    








