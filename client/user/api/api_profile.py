from .imports import *


def api_profile(request):
    user = User.get_user(request.GET.get('cellphone'))
    user.cellphone = request.GET.get('cellphone')
    user.first_name = request.GET.get('first_name')
    user.last_name = request.GET.get('last_name')
    user.email = request.GET.get('email')
    if user.cellphone and user.is_anonymous:
        user.login(request)
        user.save()
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)
