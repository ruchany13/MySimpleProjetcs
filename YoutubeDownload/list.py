from pytube import Playlist, YouTube
# we can see playlist with Playlist. Video variable have every video url once.
# but I can't download with video.streams..., so I use Youtube() 
#pl = input("Url:")
location = input("Location:")
playlist = Playlist("https://www.youtube.com/watch?v=7654-VMsWdI&list=PLnCAl6KpLMBPW1ahw1obWJI16oP7qLX6O")
# video = "https:", video variable have url
for video in playlist:
    yt = YouTube(video)
    print("Downloading  :",yt.title)
    yt.streams.get_highest_resolution().download()
    print("Downloaded  :", yt.title)
    
    
