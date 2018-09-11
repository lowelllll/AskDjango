from django import forms
from askdjango.widgets.naver_map_point_widget import  NaverMapPointWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat':NaverMapPointWidget, # 위젯 추가
        }

