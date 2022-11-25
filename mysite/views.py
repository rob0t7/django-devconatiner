from django.http import HttpResponse, HttpRequest


def live(_request: HttpRequest) -> HttpResponse:
    return HttpResponse("OK")
