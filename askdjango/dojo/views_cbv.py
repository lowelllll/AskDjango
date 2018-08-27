# dojo/views_cbv.py

import os
from django.conf import settings
from django.views.generic import View,TemplateView
from django.http import HttpResponse,JsonResponse

# CBV

class PostListView1(View):
    def get(self,request):
        name = '예진'
        html = self.get_template_string(name)
        return HttpResponse(html)

    def get_template_string(self,name):
        return  '''
            <h1>AskDjango</h1>
            {name}
        '''.format(name=name)
    
    # FBV와 다르게 OOP 가능

post_list1 = PostListView1.as_view() # 함수 반환

class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'

    def get_context_data(self, **kwargs):
        # context = super(PostListView2, self).get_context_data() python2
        context = super().get_context_data()
        context['name'] = '예진'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(View):
    # JSON 형식 응답
    def get(self,request):
        return JsonResponse(self.get_data(),json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {
            'message':'안녕 장고',
            'items':['파이썬','장고']
        }

post_list3 = PostListView3.as_view()

class ExcelDownload(View):
    # 엑셀 다운로드
    excel_path = os.path.join(settings.BASE_DIR,'sample_excel_denmark.xlsx')

    def get(self,request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path,'rb') as f:
            response = HttpResponse(f,content_type='application/cnd.ms-excel')
            # 응답 헤더 셋팅
            response['Content-Disposition'] = 'attachment; filename = "{}"'.format(filename)
            return response

excel_download = ExcelDownload.as_view()
