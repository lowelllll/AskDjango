# dojo/forms.py
from django import forms
from .models import Post,GameUser



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','user_agent'] # '__all__'
        widgets = {
            'user_agent':forms.HiddenInput,
        }
        
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

class GameUserSignupForm(forms.ModelForm): # Form 유효성 실습을 위한 form
    class Meta:
        model = GameUser
        fields =  ['server_name','username']

    def clean_username(self):
        "값 변환은 clean 함수에서만 가능함. validator에서는 지원하지 않음."
        return self.cleaned_data.get('username','').strip() # username 필드 값의 좌/우 공백을 제거하고 반환.