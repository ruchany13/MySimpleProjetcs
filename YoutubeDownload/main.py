from pytube import YouTube
print("Welcoe to Youtube Downloader")

url = input("Youtube link :")
yt = YouTube(url)

location = input("Path Location:")


print("Downloading:", yt.title)
yt.streams.get_highest_resolution().download(output_path=location)
print("Download: ", yt.title)



