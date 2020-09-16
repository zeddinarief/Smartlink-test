from django.http import JsonResponse


class Response:

    def base(self, values=None, message="", status=200):
        return JsonResponse(values, status=status)

    @staticmethod
    def ok(values=None):
        return Response().base(values=values, status=200)

    @staticmethod
    def badRequest(values=None, status=400):
        return Response().base(values=values, status=status)

    @staticmethod
    def unauthorized(message="Unauthorized!"):
        return Response().base(values={"message": message}, status=400)