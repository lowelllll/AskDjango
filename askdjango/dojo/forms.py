# dojo/forms.py
from django import forms
from .models import Post

def min_length_3_validator(value): # 유효값 검사 함수 생성.
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    def save(self,commit = True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post