from django.shortcuts import render
from .decorators import bot
from . import functions

@bot
def on_init(request): # 유저가 최초로 채팅방에 들어오거나 채팅방을 재 진입시 호출
    return {'type': 'text'}
@bot
def on_message(request): # 답장 
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content'] # photo 타입일 경우에는 이미지 URL

    if content.startswith('멜론검색:'):
        query = content[6:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)
    else:
        response = '지원하는 명령어가 아닙니다.'
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



