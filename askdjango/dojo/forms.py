# dojo/forms.py
from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content'] # '__all__'
        
        # validator는 model에서 적용

    """model field
    modelform.save
    commit = false instance.save() 함수 호출을 지연시고자할 때 사용.
    
    def save(self,commit = True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance    
    """


    """ form field

     title = forms.CharField(validators=[min_length_3_validator])
     content = forms.CharField(widget=forms.Textarea)

      def save(self,commit = True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
    """
