import re
from django import forms
from django.template.loader import render_to_string

from django.conf import settings # django/conf/global_settings.py + askdjango/settings.py

class NaverMapPointWidget(forms.TextInput):
    BASE_LAT , BASE_LNG = '37.4974991','127.0282464' # 강남역

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'naver_client_id': settings.NAVER_CLIENT_ID,
            'id':attrs['id'],
            'base_lat':self.BASE_LAT,
            'base_lng':self.BASE_LNG,
        }

        if value: # 값이 있으면 (수정)
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+',value) # 정규식 검사.
                context.update({'base_lat':lat,'base_lng':lng})
            except (IndexError,ValueError):
                pass

        html = render_to_string('widgets/naver_map_point_widget.html',context) # render는 HttpResponse 객체 반환, render_to_string은 템플릿을 문자열로 반환.

        attrs['readonly'] = 'readonly'

        parenet_html = super().render(name, value, attrs) # 부모 호출

        return parenet_html + html