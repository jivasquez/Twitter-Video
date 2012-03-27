from django.shortcuts import render_to_response

from twitter_video.dbmodels.video import Video
from twitter_video import VIDEO_DIR

def upload_video(request):
    if request.method == 'POST':
        print request.POST['title']
        video = Video.objects.create(
            path = 'prueba',
            title = request.POST['title'],
            latitude = 'prueba',
            longitude = 'prueba',
            timestamp = 'prueba',
            user = 'prueba')
        video.path = '/media/'+ video.id + '.mp4'
        video.save()
        content_type = request.FILES['video'].content_type
        print "content_type", content_type
        destination = open(VIDEO_DIR+video.id+'.mp4', 'wb+')
        for chunk in request.FILES['video'].chunks():
            destination.write(chunk)
        destination.close()
    return render_to_response('upload.html', {})

def upload_form(request):
    response = render_to_response('upload.html', {})
    return response