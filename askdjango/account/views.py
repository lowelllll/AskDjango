# account/views.py
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from .forms import SignupForm

@login_required # 로그인 되어있는 상태여야만 뷰를 호출할 수 있음./ 로그인 되어있지 않으면 로그인 url로 이동
def profile(request):
    return render(request,'account/profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request,'account/signup_form.html',{'form':form})