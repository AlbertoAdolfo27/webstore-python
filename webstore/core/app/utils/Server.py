from array import array

from django.urls import reverse


class Server:
    SERVER_ROOT = 'http://127.0.0.1:8080'

    @classmethod
    def get_url(cls, path_name: str = 'api:category-list', args: array = []):
        return cls.SERVER_ROOT + reverse(path_name, args=args)


