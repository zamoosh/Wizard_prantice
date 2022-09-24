from .imports import *


def videos(request):
    context = {}
    context['video'] = Video.objects.first()
    print(f'{__name__.replace(".", "/")}.html')
    return render(request, f'{__name__.replace(".", "/")}.html', context)
