from django.http import JsonResponse


def getRoutes(request):
    data = {
        'hello': [1,2,3,4],
    }

    return JsonResponse(data, safe=False)