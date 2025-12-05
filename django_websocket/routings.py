from django.urls import path
from apps.home.consumers import ChatConsumer  # 导入自定义的处理websocket请求的视图

urlpatterns = [
    path('ws/test/', ChatConsumer.as_asgi()),  # ws/test/请求，由自定义的websocket视图处理
]