from django.core.files import File
from os.path import basename
import requests
from django.shortcuts import render
from .decorators import bot
from . import functions
from .models import Post

@bot
def on_init(request): # 유저가 최초로 채팅방에 들어오거나 채팅방을 재 진입시 호출
    return {'type': 'text'}
@bot
def on_message(request): # 답장
    user_key = request.JSON['user_key']
    type = request.JSON['type'] # user가 보낸 text
    content = request.JSON['content'] # photo 타입일 경우에는 이미지 URL

    if type == 'photo':
        img_url = content
        img_name = basename(img_url)
        res = requests.get(img_url, stream=True) # 파일 오브젝트를 넘기기 위해 stream 사용
        post = Post(user=request.user)
        post.photo.save(img_name,File(res.raw))
        post.save()
        response = '사진을 저장했습니다.'
    else:
        post = Post.objects.create(user=request.user, message=content)
        response = '포스팅을 저장했습니다.'

    return {
        'message': {
            'text': response,
        }
    }

def on_added(request): # 유저가 친구로 추가할 경우 호출
    user_key = request.JSON['user_key'] 


def on_block(request): # 유저가 차단할 경우 호출
    return {}

def on_leave(request): # 유저가 채팅방에서 나갈 경우 호출
    return {}

def post_list(request, user_key):
    qs = Post.objects.filter(user__username=user_key)
    return render(request,'plusfriend/post_list.html',{'qs':qs})
