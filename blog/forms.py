from turtle import title
from xml.etree.ElementTree import Comment
from django import forms
import django
from blog.models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields  = ('title', 'author', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }