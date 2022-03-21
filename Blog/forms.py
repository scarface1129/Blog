from django import forms
from .models import Blogs, Likes


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs 
        fields = [
            
            'user',
            'title',
            'content',
                    
        ]   


class BlogForm(forms.ModelForm):
    class Meta:
        model = Likes 
        fields = [
            
            'post',
            'status',
                    
        ]   