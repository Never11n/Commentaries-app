import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CommentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['comments']

        self.send(text_data=json.dumps({
            'comments': comment
        }))
