import requests


class UserService:
    endpoint = 'http://localhost:8001/api/'

    @staticmethod
    def get(path, **kwargs):
        headers = kwargs.get('headers', [])
        return requests.get(UserService.endpoint + path, headers=headers).json()

    @staticmethod
    def post(path, **kwargs):
        headers = kwargs.get('headers', [])
        data = kwargs.get('data', [])
        return requests.post(UserService.endpoint + path, data=data, headers=headers).json()

    @staticmethod
    def put(path, **kwargs):
        headers = kwargs.get('headers', [])
        new_head={}
        new_head['Cookie'] = kwargs.get('headers', [])['Cookie']
        data = kwargs.get('data', [])
        return requests.put(UserService.endpoint + path, data=data, headers=new_head).json()


