from django import forms
from .models import Post,Comment

from django_summernote.admin import SummernoteModelAdmin,SummernoteWidget,SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']