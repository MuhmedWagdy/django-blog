from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


from .models import Post,Comment
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
