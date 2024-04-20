from django.shortcuts import render
from django.http import JsonResponse
from googleapiclient.discovery import build
from django.conf import settings
from .models import CachedAPIRequest
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    user_id = request.user.id

    search_history = CachedAPIRequest.objects.filter(
        user_id = user_id,
    ).order_by('-created_at')[:3]
    context = {
        'search_history' : search_history,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def search_videos(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        #Check
        cached_request = CachedAPIRequest.objects.filter(
            endpoint='youtube_search',
            request_data=search_query
        ).first()

        if cached_request:
            #If Found
            videos = cached_request.response_data
        else:
            #Not Found
            youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
            search_response = youtube.search().list(
                q=search_query,
                part='snippet',
                type='video'
            ).execute()
            videos = []
            for search_result in search_response.get('items', []):
                videos.append({
                    'title': search_result['snippet']['title'],
                    'video_id': search_result['id']['videoId']
                })
            #Store
            CachedAPIRequest.objects.create(
                user = request.user,
                endpoint='youtube_search',
                request_data=search_query,
                response_data=videos
            )
        return render(request, 'home.html', {'videos': videos})

def previous_search_videos(request, req):
    if request.method == 'GET':
        search_query = req
        #Check
        cached_request = CachedAPIRequest.objects.filter(
            endpoint='youtube_search',
            request_data=search_query
        ).first()

        if cached_request:
            #If Found
            videos = cached_request.response_data
        else:
            #Not Found
            youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
            search_response = youtube.search().list(
                q=search_query,
                part='snippet',
                type='video'
            ).execute()
            videos = []
            for search_result in search_response.get('items', []):
                videos.append({
                    'title': search_result['snippet']['title'],
                    'video_id': search_result['id']['videoId']
                })
            #Store
            CachedAPIRequest.objects.create(
                user = request.user,
                endpoint='youtube_search',
                request_data=search_query,
                response_data=videos
            )
        return render(request, 'home.html', {'videos': videos})




