from django.http import HttpResponse, JsonResponse


def ping(request):
    return JsonResponse({'ping': 'pong'})
