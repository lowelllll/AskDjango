from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile

class SignupForm(UserCreationForm): # 회원가입 폼에 필드 추가
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) # 기존 필드에 이메일 필드 추가.

    def save(self, commit=True):
        user = super().save() # user 저장
        Profile.objects.create( # profile 인스턴스 저장.
            user = user,
            phone_number= self.cleaned_data['phone_number'], # 유효성 검사를 마친 후 반환되는 cleaned_data
            address = self.cleaned_data['address']
        )
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label = "3+3=?") # 퀴즈를 맞춰야 로그인 수행.

    def clean_answer(self):
        answer = self.cleaned_data.get('answer',None)
        if answer != 6:
            raise forms.ValidationError('mismatched!')
        return answer

