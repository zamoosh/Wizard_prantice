from .imports import *


def api_profile(request):
    print('\n\n\n\n zamoosh \n\n\n\n')
    print(request.GET.get('first_name'))
    print(request.GET.get('last_name'))
    print(request.GET.get('email'))
    print(request.GET.get('data'))
    return JsonResponse({}, status=200)
