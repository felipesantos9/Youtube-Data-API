from googleapiclient.discovery import build

youTubeApiKey = "AIzaSyCCgzIOU3uvkJIjBWcP21Skay15pZ3PgdY"

youtube = build('youtube', 'v3', developerKey=youTubeApiKey)

channel_response = youtube.channels().list(part='id', forUsername='Formula1').execute()

channel_id = channel_response["items"][0]["id"]

channel_playlists = youtube.playlists().list(part=['snippet','contentDetails'],channelId=channel_id, maxResults=50 ).execute()

for playlist in channel_playlists['items']:
    if "Formula 1" in playlist['snippet']['title'] and "2023" in playlist['snippet']['title']:
        print(playlist['snippet']['title'])