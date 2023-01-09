from django.shortcuts import render

def show(request):
    return render(request, 'showVideo.html', {'url':'static/ListVideo/videoplayback.mp4'})
