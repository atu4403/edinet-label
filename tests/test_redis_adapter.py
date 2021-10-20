from src.edinet_label.redis_adapter import redis_client


def test_redis_client():
    r = redis_client(0)
    r.set('key1', 'value1')

    assert r.get('key1') == 'value1'

    r.hset('hash_key1', 'member1', 'hash_value1')
    r.hset('hash_key1', 'member2', 'hash_value2')

    assert r.hget('hash_key1', 'member1') == 'hash_value1'
    assert r.hgetall('hash_key1') == {'member1': 'hash_value1', 'member2': 'hash_value2'}
