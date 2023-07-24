from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['author','draft']
    search_fields = ['content','title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post','create_at']
    list_filter = ['user']



from .models import Post,Comment
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
