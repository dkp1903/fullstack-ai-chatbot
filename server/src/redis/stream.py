
class StreamConsumer:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def consume_stream(self, block: int,  stream_channel):
        response = self.redis_client.xread(
            streams={stream_channel:  '0-0'}, block=block)

        return response

    def delete_message(self, stream_channel, message_id):
        self.redis_client.xdel(stream_channel, message_id)
