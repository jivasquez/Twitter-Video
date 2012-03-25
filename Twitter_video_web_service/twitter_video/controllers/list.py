from django.shortcuts import render_to_response

from twitter_video.dbmodels.video import Video

def list_videos(request):
    
    videos = Video.objects.all()
    return render_to_response('list.html', {'videos': videos})

def api_list_videos(request):
    videos = Video.objects.all()
    print "video", videos[0]
    return render_to_response('api_list.html', {'videos': videos})