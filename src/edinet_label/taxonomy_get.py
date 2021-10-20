from .redis_adapter import redis_client


def get_label(place: str, name: str):
    if not place.startswith('taxonomy'):
        ref = place.split('taxonomy/')
        if len(ref) == 1:
            return None
        place = f'taxonomy/{ref[-1]}'
    r = redis_client()
    return r.hget(place, name)
