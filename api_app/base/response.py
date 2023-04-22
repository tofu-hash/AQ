from rest_framework.response import Response
from rest_framework import status


class CustomResponse:
    def __init__(self, data=None, message: str = 'Ответ без сообщения.'):
        if data is None:
            data = {}
        self.data = data
        self.message = message

    def bad(self, _status: status = None, **kwargs) -> Response:
        data = {
            'message': self.message,
            'data': self.data
        }
        if _status is None:
            _status = status.HTTP_400_BAD_REQUEST
        return Response(
            data=data,
            status=_status,
            **kwargs
        )

    def good(self, _status: status = None, **kwargs) -> Response:
        data = {
            'message': self.message,
            'data': self.data
        }
        if _status is None:
            _status = status.HTTP_200_OK
        return Response(
            data=data,
            status=_status,
            **kwargs
        )
