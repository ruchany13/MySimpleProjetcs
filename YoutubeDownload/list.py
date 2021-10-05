import time
def func(pl, location):
    from pytube import Playlist, YouTube
    # we can see playlist with Playlist. Video variable have every video url once.
    # but I can't download with video.streams..., so I use Youtube() 
    #pl = input("Url:")
   
    playlist = Playlist(pl)
    # video = "https:", video variable have url
    for video in playlist:
        yt = YouTube(video)
        print("Downloading  :",yt.title)
        yt.streams.get_highest_resolution().download(output_path=location)
        print("Downloaded  :", yt.title)

while True:  
    try :
        pl = input("Playlist URL:  ")
        location = input("Location:")
        func(pl, location)
    except:
        print("Time start")
        time.sleep(30)
        func(pl, location)
        print("Time finish")
