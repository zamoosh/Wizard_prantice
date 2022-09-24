from django.db import models


def video_file(instance, filename):
    return "%s/%s/%s/%s" % ('video', instance.video.id, 'file', filename)


def video_caption(instance, filename):
    return "%s/%s/%s/%s" % ('video', instance.video.id, 'caption', filename)


class Video(models.Model):
    name = models.CharField(max_length=255)
    markers = models.JSONField(default=dict)


class VideoFile(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    file = models.FileField(upload_to=video_file)


class VideoCaption(models.Model):
    lang = models.CharField(max_length=10)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    file = models.FileField(upload_to=video_caption)
