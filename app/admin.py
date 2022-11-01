from django.contrib import admin
from .models import(
    Video,
    feedback,
    homepage,
    wishlist,
    Customer
)
from embed_video.admin import AdminVideoMixin
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','anime_watched']
# @admin.register(main_anime)
# class main_animeModelAdmin(admin.ModelAdmin):
#     list_display =['id','title','episode_num','episode_name','description','category','episode_thumbnail']
    
admin.site.register(wishlist)
admin.site.register(homepage)
admin.site.register(feedback)
admin.site.register(Video)
