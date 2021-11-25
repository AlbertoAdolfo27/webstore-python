from array import array, ArrayType
from django.urls import reverse


class Server:
    HTTP_HOST = 'http://127.0.0.1:8080'

    @classmethod
    def get_url(cls, path_name: str = 'api:category-list', args: array | ArrayType = None):
        # print(HttpRequest.get_host())
        return cls.HTTP_HOST + reverse(path_name, args=args)


