import redis


def redis_client(db: int = 1) -> redis.client.Redis:
    return redis.Redis(host='192.168.0.143', port=6378, db=db, decode_responses=True)
