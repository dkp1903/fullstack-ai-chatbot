from fastapi import WebSocket, status, Query
from typing import Optional
from ..redis.config import Redis

redis = Redis()


def get_token(
    websocket: WebSocket,
    token: Optional[str] = Query(None),
):

    if token is None or token == "":
        websocket.close(code=status.WS_1008_POLICY_VIOLATION)

    redis_client = redis.create_connection()
    isexists = redis_client.exists(token)

    if isexists == 1:
        return token
    else:
        websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="Session not authenticated or expired token")
