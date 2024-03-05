from googleapiclient.discovery import build

youTubeApiKey = "AIzaSyCCgzIOU3uvkJIjBWcP21Skay15pZ3PgdY"

youtube = build('youtube', 'v3', developerKey=youTubeApiKey)

channel_response = youtube.channels().list(part='id', forUsername='Formula1').execute()

channel_id = channel_response["items"][0]["id"]

print(channel_id)