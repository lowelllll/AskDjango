# accounts/views.py
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp # allauth
from allauth.socialaccount.templatetags.socialaccount import get_providers # allauth
from .forms import SignupForm,LoginForm

@login_required # 로그인 되어있는 상태여야만 뷰를 호출할 수 있음./ 로그인 되어있지 않으면 로그인 url로 이동
def profile(request):
    return render(request,'accounts/profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request,'accounts/signup_form.html',{'form':form})

def login(request):
    providers = []
    for provider in get_providers(): # 활성화된 프로바이더 목록을 가져옴 (INSTALLED_APPS 활성된 목록)
        try:
            # 실제 Provider별 Client id/secret이 등록되어있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
                      authentication_form=LoginForm,
                      template_name='accounts/login_form.html',
                      extra_context={'providers':providers})
