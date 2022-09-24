from .imports import *


def upload(request):
    if request.method == 'POST':
        v = Video.objects.get(id=1)
        VideoFile.objects.create(
            video=v,
            file=request.FILES.get('file')
        )
        return redirect(reverse('video:videos:videos'))
    return render(request, f'{__name__.replace(".", "/")}.html')
