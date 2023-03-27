# chat/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def index(request, room_name):
    return render(request, 'index.html', {
        'room_name': room_name
    })

@csrf_exempt
def save_drawing(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        data = json.loads(request.POST.get('data'))

        # 그림 데이터를 데이터베이스에 저장
        Drawing.objects.create(room_name=room_name, data=data)

        # 채널 레이어에서 해당 그룹의 연결된 소켓에게 메시지 전송
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'drawing_%s' % room_name,
            {
                'type': 'draw_message',
                'data': data
            }
        )

    return HttpResponse(status=200)