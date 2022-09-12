from django.contrib import admin
from .models import testimonie,feedback,Post,Gallery,Content

admin.site.site_header = " unified German language_center Admin page "
admin.site.index_title = " Admin control_Panel "

class testimoniesAmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','write_up','date_added')

class feedbackAmin(admin.ModelAdmin):
    list_display = ('name','email','message', 'feedback_date')

class PostAmin(admin.ModelAdmin):
    list_display = ('write_post', 'photo', 'date_written')

class GalleryAmin(admin.ModelAdmin):
    list_display = ('photo', 'date_uploaded')

class ContentsAmin(admin.ModelAdmin):
    list_display = ('phone_number', 'address', 'business_days', 'mail', 'about')


admin.site.register(testimonie,testimoniesAmin)
admin.site.register(feedback,feedbackAmin)
admin.site.register(Post,PostAmin)
admin.site.register(Gallery,GalleryAmin)
admin.site.register(Content,ContentsAmin)

