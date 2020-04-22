from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('title','text','category',)


    def clean_title(self):
        t=self.cleaned_data['title']
        
        if len(t) < 5:
            raise forms.ValidationError("panjang title Kurang dari 5 ")

        return t   
            

class CommentForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=('user','body',)