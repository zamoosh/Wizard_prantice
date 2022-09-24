from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from video.models import VideoFile
import os


@csrf_exempt
def chunk_upload(request):
    if request.method == 'POST':
        # doc_pattern = DocumentPattern.objects.get(id=int(request.POST.get('document_pattern_size')))
        # max_size = doc_pattern.size * 1048576
        file = request.FILES['file'].read()
        file_name = request.POST['filename']
        # if not file_name.split('.')[-1] in accepted_types:
        #     return JsonResponse({'data': 'لطفا فرمت مناسب را انتخاب کنید!'}, status=400)
        existing_path = request.POST['existingPath']
        end = request.POST['end']
        next_slice = request.POST['nextSlice']

        if file == "" or file_name == "" or existing_path == "" or end == "" or next_slice == "":
            res = JsonResponse({'data': 'Invalid Request'})
            return res
        else:
            if existing_path == 'null':
                video_file = VideoFile(video_id=1)
                video_file.title = request.POST.get('title')
                video_file.file.name = file_name
                video_file.save()
                path = os.path.join(settings.MEDIA_ROOT, 'video', 'file', str(video_file.id), file_name)
                if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'video', 'file', str(video_file.id))):
                    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'video', 'file', str(video_file.id)))
                    os.chmod(os.path.join(settings.MEDIA_ROOT, 'video', 'file', str(video_file.id)), 0o755)
                with open(path, 'wb+') as destination:
                    destination.write(file)
                video_file.file.name = os.path.join('document', str(video_file.id), file_name)
                # if video_file.file.width >= doc_pattern.extra.get('width') and video_file.file.height >= doc_pattern.extra.get('height'):
                #     return JsonResponse({'data': 'لطفا فایلی با ابعاد مناسب انتخاب کنید!'}, status=400)
                video_file.save()
                if int(end):
                    res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': video_file.file.name})
                else:
                    res = JsonResponse({'existingPath': video_file.file.name})
                return res

            else:
                path = os.path.join(settings.MEDIA_ROOT, existing_path)
                video_file = VideoFile.objects.get(file=existing_path)
                if video_file.file.name.split("/")[-1] == file_name:
                    if not video_file.eof:
                        with open(path, 'ab+') as destination:
                            destination.write(file)
                        # if video_file.file.size >= max_size:
                        #     return JsonResponse({'size': False}, status=400)
                        if int(end):
                            video_file.eof = int(end)
                            video_file.save()
                            res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': video_file.file.name})
                        else:
                            res = JsonResponse({'existingPath': video_file.file.name})
                        return res
                    else:
                        res = JsonResponse({'data': 'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data': 'No such file exists in the existingPath'})
                    return res
    return JsonResponse({'data': 'nothing'}, status=200)
