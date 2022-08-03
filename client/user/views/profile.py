from .imports import *


def profile(request):
    return render(request, f'{__name__.replace(".", "/")}.html')
