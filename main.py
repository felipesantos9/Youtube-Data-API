from googleapiclient.discovery import build

youTubeApiKey = "AIzaSyCCgzIOU3uvkJIjBWcP21Skay15pZ3PgdY"

youtube = build('youtube', 'v3', developerKey=youTubeApiKey)

channel_response = youtube.channels().list(part='id', forUsername='Formula1').execute()

channel_id = channel_response["items"][0]["id"]

channel_playlists = youtube.playlists().list(part=['snippet','contentDetails'],channelId=channel_id, maxResults=50 ).execute()

playlists_ids = []
for playlist in channel_playlists['items']:
    if "Formula 1" in playlist['snippet']['title'] and "2023" in playlist['snippet']['title']:
        playlists_ids.append(playlist['id'])

videos_ids = {}
for id in playlists_ids:
    playlist_items = youtube.playlistItems().list(part=['snippet','contentDetails'], playlistId=id, maxResults=1).execute()
    
    title = playlist_items['items'][0]['snippet']['title']
    video_id = playlist_items['items'][0]['contentDetails']['videoId']
    videos_ids[title] = video_id

for title, id in videos_ids.items():
    video_statistics = youtube.videos().list(part="statistics", id=id).execute()
    views = video_statistics['items'][0]['statistics']['viewCount']
    videos_ids[title] = int(views)

views = videos_ids.values()
tuple_views = tuple(views)

count = 0
for views in sorted(tuple_views, reverse=True):
    count +=1

    for title, value in videos_ids.items():
        if views == value:
            print(f"{count}. {title}: {views}")
        
            if count == 1:
                most_viewed_title = title
                most_viewed_views = views

print(f"O highlight mais visto foi {most_viewed_title}, com {most_viewed_views} visualizações")
    

    