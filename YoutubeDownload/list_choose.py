from pytube import Playlist, YouTube
print("Welcome to the Youtube Download...\n If you want download video press 1")

#url = input("Playlist Url :")
#location = input("Location :")

playlist = Playlist("https://www.youtube.com/playlist?list=PLh9ECzBB8tJPFTpuHKhYayis0H9pS6_rI")
i=0
videos = []
for video in playlist:
    yt = YouTube(video)
    i+=1
    v = "1 for download {}:".format(yt.title)
    control = input(v)
    
    if control == "1":
        videos.append(video)
    else:
        pass

print(videos)
print(video)

for i in videos:
    yt =YouTube(i)
    print("Downloading", yt.title)
    yt.streams.get_highest_resolution().download()
    print("Download ",yt.title)
    


